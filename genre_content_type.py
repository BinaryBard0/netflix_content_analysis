import pandas as pd
import matplotlib.pyplot as plt

# Load the prepared dataset
file_path = 'F:/Data Analyst Project/Netflix/netflix_titles/prepared_netflix_titles.csv'            
netflix_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print(netflix_data.head())

# View the column names to identify genre columns
print(netflix_data.columns)


# Assuming you have multiple genre columns (binary representation: 0/1)
genre_columns = ['Action & Adventure', 'Anime Features', 'Anime Series', 'British TV Shows', 'Children & Family Movies', 'Classic & Cult TV', 'Classic Movies', 'Comedies', 'Crime TV Shows', 'Cult Movies', 'Documentaries', 'Docuseries', 'Dramas', 'Faith & Spirituality', 'Horror Movies', 'Independent Movies', 'International Movies', 'International TV Shows', "Kids' TV", 'Korean TV Shows', 'LGBTQ Movies', 'Movies', 'Music & Musicals', 'Reality TV', 'Romantic Movies', 'Romantic TV Shows', 'Sci-Fi & Fantasy', 'Science & Nature TV', 'Spanish-Language TV Shows', 'Sports Movies', 'Stand-Up Comedy', 'Stand-Up Comedy & Talk Shows', 'TV Action & Adventure', 'TV Comedies', 'TV Dramas', 'TV Horror', 'TV Mysteries', 'TV Sci-Fi & Fantasy', 'TV Shows', 'TV Thrillers', 'Teen TV Shows', 'Thrillers']


# Initialize an empty DataFrame to store genre counts for Movies and TV Shows
genre_counts = pd.DataFrame()

# Loop through each genre column and group by content type (Movies/TV Shows)
for genre in genre_columns:
    counts = netflix_data.groupby('type')[genre].sum()  # Summing binary values for Movies and TV Shows
    genre_counts[genre] = counts

# Transpose the DataFrame for easier plotting
genre_counts = genre_counts.T

# Create a stacked bar chart for genre analysis
plt.figure(figsize=(20, 10))

# Plot stacked bars: first plot Movies, then TV Shows stacked on top
plt.bar(genre_counts.index, genre_counts['Movie'], label='Movies', color='#1f77b4')
plt.bar(genre_counts.index, genre_counts['TV Show'], bottom=genre_counts['Movie'], label='TV Shows', color='#ff7f0e')

# Add labels and title
plt.xlabel('Genre', fontsize=14)
plt.ylabel('Number of Titles', fontsize=14)
plt.title('Stacked Bar Chart of Movies vs TV Shows by Genre', fontsize=18)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90, ha='center', fontsize=10)

# Add legend
plt.legend()

# Increase the top margin to prevent cutting off bars
plt.ylim(0, genre_counts.values.max() * 1.1)

# Show the plot
plt.tight_layout()
plt.show()
