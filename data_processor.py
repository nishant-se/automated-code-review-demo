import pandas as pd
from math_utils import fibonacci

def clean_data(df):
    df.dropna(inplace=True)
    df['created_at'] = pd.to_datetime(df['created_at'])
    return df

def add_fib_column(df):
    df['fib_score'] = df['score'].apply(fibonacci)
    return df
