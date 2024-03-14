import os
import pandas as pd
import settings
import csv

# Iterate over all files in the directory
for filename in os.listdir(settings.csv_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(settings.csv_dir, filename)
        print(file_path)
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Convert column names to lowercase
        df.columns = [col.lower() for col in df.columns]

        # Save the modified DataFrame back to CSV
        df.to_csv(file_path, quoting=csv.QUOTE_NONNUMERIC, index=False)
