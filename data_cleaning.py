# Import necessary libraries
import pandas as pd

# Load the dataset from a CSV file
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

# Display the first few rows of the dataset``
print(netflix_data.head())

# Check for missing values
print(netflix_data.info())
print(netflix_data.isnull().sum())

# Remove rows with missing values in 'date_added', 'rating', and 'duration'
netflix_data_cleaned = netflix_data.dropna(subset=['date_added', 'rating', 'duration'])

# Mark missing values as 'Unknown' in 'director', 'cast', and 'country'
netflix_data_cleaned.loc[:, 'director'] = netflix_data_cleaned['director'].fillna('Unknown')
netflix_data_cleaned.loc[:, 'cast'] = netflix_data_cleaned['cast'].fillna('Unknown')
netflix_data_cleaned.loc[:, 'country'] = netflix_data_cleaned['country'].fillna('Unknown')

# Verify there are no missing values left
print(netflix_data_cleaned.isnull().sum())

# Save the cleaned dataset to a new CSV file
netflix_data_cleaned.to_csv('F:/Data Analyst Project/Netflix/netflix_titles/cleaned_netflix_titles.csv', index=False)

