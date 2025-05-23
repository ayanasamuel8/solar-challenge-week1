import pandas as pd
import numpy as np
import os

def clean_solar_data(input_file, output_file):
    """
    Clean solar radiation data from raw CSV files.
    
    Parameters:
    -----------
    input_file : str
        Path to the raw data CSV file
    output_file : str
        Path where the cleaned data will be saved
    """
    print(f"Cleaning data from {input_file}...")
    
    # Read the raw data
    df = pd.read_csv(input_file)
    
    # Standardize column names
    df.columns = df.columns.str.strip().str.upper()
    
    # Ensure required columns exist
    required_columns = ['GHI', 'DNI', 'DHI']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    # Remove rows with missing values in key columns
    df = df.dropna(subset=required_columns)
    
    # Remove physically impossible values
    df = df[df['GHI'] >= 0]
    df = df[df['DNI'] >= 0]
    df = df[df['DHI'] >= 0]
    
    # Add basic quality checks
    df = df[df['GHI'] >= df['DHI']]  # GHI should be greater than or equal to DHI
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")
    print(f"Original shape: {len(df)} rows")
    print(f"Final shape: {len(df)} rows")

def main():
    # Define data paths
    countries = ['benin', 'sierra_leone', 'togo']
    
    for country in countries:
        input_file = f'data/raw/{country}_solar.csv'
        output_file = f'data/{country}_clean.csv'
        
        if os.path.exists(input_file):
            try:
                clean_solar_data(input_file, output_file)
            except Exception as e:
                print(f"Error processing {country} data: {str(e)}")
        else:
            print(f"Warning: Raw data file for {country} not found at {input_file}")

if __name__ == '__main__':
    main() 