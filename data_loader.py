import pandas as pd

def load_cyclone_data(file_path):
    """Load cyclone data from a CSV file."""
    df = pd.read_csv('tropical_cyclone_data.csv')
    # Split the dataframe into train and test sets based on a specific criterion
    # Here, we assume the split is based on some column values or a predefined split
    # Replace this with actual logic for your dataset
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
    # Path to your downloaded CSV file
    file_path = 'tropical_cyclone_data.csv'
    
    # Load and process the data
    df_train, df_test = load_cyclone_data(file_path)
    df_train = process_data(df_train)
    df_test = process_data(df_test)
    
    # Save the processed data to CSV files
    df_train.to_csv('processed_train.csv', index=False)
    df_test.to_csv('processed_test.csv', index=False)



