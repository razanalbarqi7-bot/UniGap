import os
import pandas as pd
from core.cleaning import clean_data

os.makedirs("output", exist_ok=True)

try:
    df = pd.read_csv("data/UniGap_edge_cases.csv")
    original_rows = len(df)
    cleaned_df = clean_data(df)
    cleaned_rows = len(cleaned_df)
    cleaned_df.to_csv("output/UniGap_edge_cases_cleaned.csv", index=False)
    print(f"test file: {original_rows} rows -> {cleaned_rows} rows after cleaning")
except Exception as e:
    print(f"Error processing edge cases: {e}")

print("Saved the cleaned files in the output folder")
