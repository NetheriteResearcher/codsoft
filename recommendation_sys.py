import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (can be expanded with a larger dataset like MovieLens)
data = {
    'movie_title': [
        'Inception', 'Interstellar', 'The Dark Knight', 'Memento', 'The Matrix',
        'Fight Club', 'The Godfather', 'Pulp Fiction', 'Shutter Island', 'Se7en'
    ],
    'description': [
        'A thief who enters the dreams of others to steal secrets.',
        'A team of explorers travel through a wormhole in space.',
        'A vigilante superhero fights crime in Gotham City.',
        'A man with short-term memory loss uses tattoos to track information.',
        'A computer hacker discovers a shocking reality about the world.',
        'An office worker forms an underground fight club.',
        'The aging patriarch of a mafia family transfers control to his son.',
        'The lives of two hitmen, a boxer, and a gangster intertwine.',
        'A detective investigates a mental institution for the criminally insane.',
        'Two detectives hunt a serial killer who uses the seven deadly sins.'
    ],
    'genre': [
        'Sci-Fi, Thriller', 'Sci-Fi, Drama', 'Action, Thriller', 'Mystery, Thriller',
        'Sci-Fi, Action', 'Drama, Thriller', 'Crime, Drama', 'Crime, Drama',
        'Mystery, Thriller', 'Crime, Thriller'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Combine description + genre for better matching
df['features'] = df['description'] + ' ' + df['genre']

# Convert text into TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['features'])

# Compute cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix)

def recommend_movies(movie_name, num_recommendations=5):
    """Recommend movies based on similarity to the given movie name."""
    if movie_name not in df['movie_title'].values:
        return f"Movie '{movie_name}' not found. Try another one."

    movie_index = df[df['movie_title'] == movie_name].index[0]
    similarity_scores = list(enumerate(cosine_sim[movie_index]))
    sorted_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:num_recommendations+1]
    
    recommended_movies = [df.iloc[i[0]]['movie_title'] for i in sorted_movies]
    return {"Input Movie": movie_name, "Recommended Movies": recommended_movies}

# Test the recommendation system
user_movie = "Inception"  # Change this to test different movies
recommendations = recommend_movies(user_movie)
print(recommendations)