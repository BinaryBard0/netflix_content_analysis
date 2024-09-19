import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the prepared dataset
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/prepared_netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(netflix_data.head())

# Group by country and type (Movies vs TV Shows) and count the number of entries
country_content_type = netflix_data.groupby(['country', 'type']).size().unstack(fill_value=0)

# Sort by the total number of content items in each country
country_content_type['Total'] = country_content_type.sum(axis=1)
country_content_type = country_content_type.sort_values(by='Total', ascending=False)

# View the top N countries by content count (let's say top 10)
top_countries = country_content_type.head(10)

# Calculate the percentage of Movies and TV Shows for each country
top_countries['Movie %'] = (top_countries['Movie'] / top_countries['Total']) * 100
top_countries['TV Show %'] = (top_countries['TV Show'] / top_countries['Total']) * 100

# Create a bar chart for the top 10 countries
plt.figure(figsize=(12, 7))

# Bar width for side-by-side comparison
bar_width = 0.35
index = np.arange(len(top_countries))

# Plot side-by-side bar chart for Movies and TV Shows
plt.bar(index, top_countries['Movie'], bar_width, label='Movies', color='#1f77b4')
plt.bar(index + bar_width, top_countries['TV Show'], bar_width, label='TV Shows', color='#ff7f0e')

# Add labels and title
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Titles', fontsize=14)
plt.title('Distribution of Movies vs TV Shows by Country (Top 10 Countries)', fontsize=18)

# Add country labels to the x-axis
plt.xticks(index + bar_width / 2, top_countries.index, rotation=45, ha='right')

# Add the legend
plt.legend()

# Show the final plot
plt.tight_layout()
plt.show()




### HEATMAP ###
# Create a heatmap to visualize the content distribution across the top countries
plt.figure(figsize=(12, 7))
sns.heatmap(top_countries[['Movie', 'TV Show']], annot=True, cmap='coolwarm', fmt='g')

# Add labels and title
plt.xlabel('Content Type', fontsize=14)
plt.ylabel('Country', fontsize=14)
plt.title('Heatmap of Movies vs TV Shows Distribution by Country (Top 10)', fontsize=18)

# Show the final plot
plt.tight_layout()
plt.show()
