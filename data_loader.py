from datasets import load_dataset
import pandas as pd


def load_cyclone_data():
    dataset = load_dataset('torchgeo/tropical_cyclone',ignore_verifications=True)
    df_train = pd.DataFrame(dataset['train'])
    df_test = pd.DataFrame(dataset['test'])
    return df_train, df_test

import pandas as pd

def process_data(df):
    # Convert 'wind_speed' to numeric if needed
    df['wind_speed'] = pd.to_numeric(df['wind_speed'], errors='coerce')
    # Drop rows with missing values in the specified columns
    df.dropna(subset=['storm_id', 'relative_time', 'ocean', 'wind_speed'], inplace=True)
    return df


if __name__ == "__main__":
    df_train, df_test = load_cyclone_data()
    df_train = process_data(df_train)
    df_test = process_data(df_test)
    df_train.to_csv('processed_train.csv', index=False)
    df_test.to_csv('processed_test.csv', index=False)


