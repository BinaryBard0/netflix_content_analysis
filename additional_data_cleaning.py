import pandas as pd
import numpy as np

# Load the cleaned dataset
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/cleaned_netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(netflix_data.head())

# Convert 'rating' to uppercase to standardize
netflix_data['rating'] = netflix_data['rating'].str.upper().str.strip()

# Standardize 'country' names to ensure consistency
netflix_data['country'] = netflix_data['country'].str.title().str.strip()

# Check for duplicates ased on 'show_id'
duplicates = netflix_data.duplicated(subset=['show_id'])

# Display the number of duplicates found
print(f"Number of duplicate rows: {duplicates.sum()}")

#Remove duplicate rows
netflix_data = netflix_data.drop_duplicates(subset=['show_id'])

# COnvert 'date_added' to datetime format
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'], errors='coerce')

# Verify the conversion
print(netflix_data['date_added'].head())

# Check for outliers in 'release_year'
current_year = pd.Timestamp.now().year
outliers_year = netflix_data[(netflix_data['release_year'] < 1900) | (netflix_data['release_year'] > current_year)]
print(f"Outliers in 'release_year':\n{outliers_year}")

# Detect outliers in 'duration'
netflix_data[['duration_num', 'duration_unit']] = netflix_data['duration'].str.extract(r'(\d+)\s*(\w+)')
netflix_data['duration_num'] = pd.to_numeric(netflix_data['duration_num'], errors='coerce')
outliers_duration = netflix_data[netflix_data['duration_num'] > 500]  # Example threshold
print(f"Outliers in 'duration':\n{outliers_duration}")

# Extract year and month from 'date_added'
netflix_data['year_added'] = netflix_data['date_added'].dt.year
netflix_data['month_added'] = netflix_data['date_added'].dt.month

# Convert 'listed_in' (genres) to multiple binary columns (one-hot encoding)
genre_columns = netflix_data['listed_in'].str.get_dummies(sep=', ')
netflix_data = pd.concat([netflix_data, genre_columns], axis=1)

# Display the updated DataFrame
print(netflix_data.head())

# Verify consistency between 'type' and 'duration'
inconsistent_entries = netflix_data[((netflix_data['type'] == 'Movie') & (netflix_data['duration_unit'] != 'min')) |
                                    ((netflix_data['type'] == 'TV Show') & (netflix_data['duration_unit'].str.contains('Season', na=False) == False))]

print(f"Inconsistent entries based on 'type' and 'duration':\n{inconsistent_entries}")

# Clean the 'description' column
netflix_data['description'] = netflix_data['description'].str.replace(r'[^\w\s]', '', regex=True).str.strip()
netflix_data['description'] = netflix_data['description'].str.lower()

# Display cleaned description
print(netflix_data['description'].head())

# Save the further cleaned dataset
netflix_data.to_csv('F:/Data Analyst Project/Netflix/netflix_titles/further_cleaned_netflix_titles.csv', index=False)

# Impute missing 'date_added' values based on 'release_year' + 1 year
netflix_data['date_added'] = netflix_data.apply(
    lambda row: pd.Timestamp(f"{row['release_year'] + 1}-01-01") if pd.isnull(row['date_added']) else row['date_added'],
    axis=1
)

# Update 'year_added' and 'month_added' after imputation
netflix_data['year_added'] = netflix_data['date_added'].dt.year
netflix_data['month_added'] = netflix_data['date_added'].dt.month

print(netflix_data[['release_year', 'date_added', 'year_added', 'month_added']].sample(10))

print(netflix_data.info())
print(netflix_data.isnull().sum())

# Save the dataset with imputed 'date_added' as 'prepared_netflix_titles'
netflix_data.to_csv('F:/Data Analyst Project/Netflix/netflix_titles/prepared_netflix_titles.csv', index=False)
