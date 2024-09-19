import pandas as pd
import matplotlib.pyplot as plt

# Load the prepared dataset
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/prepared_netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(netflix_data.head())

# Group by release year and type (Movies vs TV Shows) and count the number of entries
yearly_content_type = netflix_data.groupby(['release_year', 'type']).size().unstack(fill_value=0)

# Calculate the total content produced each year
yearly_totals = yearly_content_type.sum(axis=1)

# Calculate the percentage of Movies and TV Shows for each year
yearly_percentage = yearly_content_type.div(yearly_totals, axis=0) * 100

# Filter out years with very few entries to avoid noise
yearly_content_type_filtered = yearly_content_type[yearly_content_type.sum(axis=1) > 10]

# Calculate the total content produced each year after filtering
yearly_totals_filtered = yearly_content_type_filtered.sum(axis=1)

# Calculate the percentage of Movies and TV Shows for each year after filtering
yearly_percentage_filtered = yearly_content_type_filtered.div(yearly_totals_filtered, axis=0) * 100


# Create a stacked area chart for better visualization of percentages
plt.figure(figsize=(12, 7))

# Plot stacked area chart
plt.stackplot(yearly_percentage_filtered.index, 
              yearly_percentage_filtered['Movie'], 
              yearly_percentage_filtered['TV Show'], 
              labels=['Movies', 'TV Shows'], 
              colors=['#1f77b4', '#ff7f0e'], 
              alpha=0.7)

# Add labels and title with bigger font size for clarity
plt.xlabel('Year', fontsize=14)
plt.ylabel('Percentage of Content (%)', fontsize=14)
plt.title('Yearly Proportion of Movies vs TV Shows on Netflix', fontsize=18)

# Add gridlines for easier reading
plt.grid(True, which='both', linestyle='--', linewidth=0.7)

# Add the legend
plt.legend(loc='upper right', fontsize=12)

# Add axis limits to focus on the most relevant data
plt.xlim(yearly_percentage_filtered.index.min(), yearly_percentage_filtered.index.max())
plt.ylim(0, 100)

# Show the final plot
plt.tight_layout()
plt.show()