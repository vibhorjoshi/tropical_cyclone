# download_dataset.py

import pandas as pd

def load_cyclone_data():
    """Load the cyclone data from a CSV file."""
    df = pd.read_csv('tropical_cyclone_data.csv')
    # Assuming the CSV file includes a 'split' column to differentiate between train and test sets
    df_train = df[df['split'] == 'train']
    df_test = df[df['split'] == 'test']
    return df_train, df_test

def process_data(df):
    """Process the cyclone data."""
    # Convert 'wind_speed' to numeric if needed
    df['wind_speed'] = pd.to_numeric(df['wind_speed'], errors='coerce')
    # Drop rows with missing values in the specified columns
    df.dropna(subset=['storm_id', 'relative_time', 'ocean', 'wind_speed'], inplace=True)
    return df

if __name__ == "__main__":
    # Load and process the data
    df_train, df_test = load_cyclone_data()
    df_train = process_data(df_train)
    df_test = process_data(df_test)
    
    # Save the processed data to CSV files
    df_train.to_csv('processed_train.csv', index=False)
    df_test.to_csv('processed_test.csv', index=False)
