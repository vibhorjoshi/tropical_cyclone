from datasets import load_dataset
import pandas as pd


def load_cyclone_data():
    dataset = load_dataset('torchgeo/tropical_cyclone')
    df_train = pd.DataFrame(dataset['train'])
    df_test = pd.DataFrame(dataset['test'])
    return df_train, df_test

def process_data(df):
    # Assume the dataset has columns 'latitude', 'longitude', 'rainfall'
    # Convert 'rainfall' to numeric if needed
    df['rainfall'] = pd.to_numeric(df['rainfall'], errors='coerce')
    df.dropna(subset=['latitude', 'longitude', 'rainfall'], inplace=True)
    return df

if __name__ == "__main__":
    df_train, df_test = load_cyclone_data()
    df_train = process_data(df_train)
    df_test = process_data(df_test)
    df_train.to_csv('processed_train.csv', index=False)
    df_test.to_csv('processed_test.csv', index=False)

