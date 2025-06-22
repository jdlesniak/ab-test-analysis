import pandas as pd
import numpy as np

from pathlib import Path
import sys

# Add src/ to path for custom module imports
project_root = Path().resolve().parents[0]
sys.path.append(str(project_root / "src"))

from paths import RAW_DATA_DIR, CLEAN_DATA_DIR

def clean_data(df):
    ### identify columns of interest
    select_cols = ['clickability_test_id', 'created_at', 'headline', 'impressions', 'clicks','winner']
    
    ### select only these columns
    df = df[select_cols]

    ### convert to datetime
    df['created_at'] = pd.to_datetime(df['created_at'], format = 'mixed')

    ### filter out bad experiments due to non-randomization
    df = df[~df['created_at'].between("2013-06-01", "2014-01-31")]

    ### identify unique number of headlines tested per test
    levels = df.groupby(['clickability_test_id'])['headline'].nunique().to_frame().reset_index()

    ### identify the 2+ tests
    tests = [levels['clickability_test_id'][i] for i in range(len(levels)) if levels['headline'][i] > 1]

    ### select only the possible tests
    df = df[df['clickability_test_id'].isin(tests)]

    ### group the data to combine impressions and clicks at the headline level
    dfgrouped = df.groupby(['clickability_test_id','headline'], as_index = False)[['impressions', 'clicks']].sum()

    ### create the proportion column for any two-prop z-tests
    dfgrouped['proportion'] = dfgrouped['clicks'] / dfgrouped['impressions']

    return dfgrouped
    
def main():
    ## read in the data
    data_path = RAW_DATA_DIR / "upworthy-archive-exploratory-packages-03.12.2020.csv"
    raw_data = pd.read_csv(data_path)

    cleaned_data = clean_data(raw_data)

    cleaned_data.to_parquet(CLEAN_DATA_DIR / "cleaned_experiments.parquet")

if __name__ == '__main__':
    main()