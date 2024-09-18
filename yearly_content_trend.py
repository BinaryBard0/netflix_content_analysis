import pandas as pd
import matplotlib.pyplot as plt

# Load the prepared dataset
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/prepared_netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(netflix_data.head())

# Assuming 'netflix_data' is your DataFrame with the Netflix titles

# Group by release year and type (Movies vs TV Shows) and count the number of entries
yearly_content_type = netflix_data.groupby(['release_year', 'type']).size().unstack(fill_value=0)

# Calculate the total content produced each year
yearly_totals = yearly_content_type.sum(axis=1)

# Calculate the percentage of Movies and TV Shows for each year
yearly_percentage = yearly_content_type.div(yearly_totals, axis=0) * 100

# Filter out years before 1950 to focus on more recent data
yearly_filtered = yearly_percentage[yearly_percentage.index >= 1950]

# Create a smoothed version of the data using a rolling window (moving average) to reduce spikes
yearly_smoothed = yearly_filtered.rolling(window=5, min_periods=1).mean()

# Create the plot
plt.figure(figsize=(10, 6))

# Plot smoothed Movies and TV Shows percentages over the years
plt.plot(yearly_smoothed.index, yearly_smoothed['Movie'], label='Movies', marker='o', color='blue', linewidth=2)
plt.plot(yearly_smoothed.index, yearly_smoothed['TV Show'], label='TV Shows', marker='o', color='orange', linewidth=2)

# Add labels, title, and a legend
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Content (%)', fontsize=12)
plt.title('Yearly Proportion of Movies vs TV Shows on Netflix (1950-Present)', fontsize=16)
plt.legend(loc='upper left')

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Display the updated plot
plt.tight_layout()
plt.show()