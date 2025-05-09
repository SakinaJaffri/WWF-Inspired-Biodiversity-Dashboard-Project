# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17g48W4mmQj1Kk-f1nGfQS1Y-ROBhLrEr
"""

# 📦 Step 1: Install required libraries
!pip install pandas openpyxl

# 📚 Step 2: Import libraries
import pandas as pd

# 📁 Step 3: Upload your Excel file
from google.colab import files
uploaded = files.upload()

# 🧾 Step 4: Load the Excel file into a DataFrame
# Replace the file name below if your file is different
file_name = list(uploaded.keys())[0]
df = pd.read_excel(file_name, sheet_name=0)

print(df.columns.tolist())

# Step 5: define the correct year columns (as integers, not strings)
years = list(range(1950, 2021))  # years as integers

# Now define the full list of columns to keep
columns_to_keep = ['Common_name', 'Region', 'Country', 'System'] + years

# Create a cleaned version of the DataFrame with just those columns
df_clean = df[columns_to_keep].copy()

# ✍️ Step 6: Rename columns for clarity
df_clean.rename(columns={
    'Common_name': 'Common Name'
}, inplace=True)

# Step 7: # Unpivot year columns into long format
df_long = df_clean.melt(
    id_vars=['Common Name', 'Region', 'Country', 'System'],
    var_name='Year',
    value_name='Population Value'
)

# Check the shape and a few rows
print(df_long.shape)
df_long.head()

# Check for missing values
df_long.isnull().sum()

# Check unique values in key columns
print("Unique Species:", df_long['Common Name'].nunique())
print("Unique Countries:", df_long['Country'].nunique())
print("Year Range:", df_long['Year'].min(), "-", df_long['Year'].max())

# Drop missing population values
df_long = df_long.dropna(subset=['Population Value'])

# Ensure data types are good
df_long['Year'] = df_long['Year'].astype(int)

# Drop any duplicates
df_long = df_long.drop_duplicates()

df_long = df_long.dropna(subset=['Population Value']).copy()
df_long['Year'] = df_long['Year'].astype(int)
df_long = df_long.drop_duplicates()

df_long['Population Value'].isnull().sum()

df_long['Year'].dtype

df_long.duplicated().sum()

df_long.sample(5)

# Export to CSV for Tableau
df_long.to_csv("cleaned_lpi_for_tableau.csv", index=False)

# Optional: Download
from google.colab import files
files.download("cleaned_lpi_for_tableau.csv")