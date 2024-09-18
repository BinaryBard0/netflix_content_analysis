import pandas as pd
import matplotlib.pyplot as plt

# Load the prepared dataset
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/prepared_netflix_titles.csv'
netflix_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(netflix_data.head())

# Calculate counts
content_type_counts = netflix_data['type'].value_counts()

# Calculate percentages
content_type_percentages = netflix_data['type'].value_counts(normalize=True) * 100

# Alternative method to create the DataFrame and rename columns
content_type_distribution = pd.DataFrame({
    'Count': content_type_counts,
    'Percentage': content_type_percentages
}).reset_index()

# Rename the columns explicitly
content_type_distribution.columns = ['Content Type', 'Count', 'Percentage']

# Colors for the pie chart
colors = ['#66b3ff', '#99ff99']

# Create the pie chart with enhanced features
plt.figure(figsize=(8, 8))

# Plot the pie chart
plt.pie(content_type_distribution['Percentage'], 
        labels=content_type_distribution['Content Type'], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=colors, 
        shadow=True, 
        explode=(0.05, 0),  # Slightly "explode" the first slice (Movies)
        wedgeprops={'edgecolor': 'black'})

# Add a legend
plt.legend(title="Content Type", loc="best")

# Add a title
plt.title('Proportion of Movies vs TV Shows on Netflix', fontsize=16)

# Display the chart
plt.tight_layout()
plt.show()


