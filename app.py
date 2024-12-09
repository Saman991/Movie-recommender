# import pandas as pd
# import streamlit as st
# import pickle
#
# # Load movie dictionary and similarity matrix
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # Convert movie_dict to DataFrame if it's not already structured that way
# if isinstance(movie_dict, dict):
#     movies = pd.DataFrame(movie_dict)
# else:
#     st.error("The 'movie_dict.pkl' file does not contain the expected dictionary structure.")
#
# def recommend(movie):
#     # Get the index of the selected movie
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     # Get a sorted list of movies based on similarity scores
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].title)
#     return recommended_movies
#
# # Streamlit UI elements
# st.title('Movie Recommender System')
# selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)
#
# if st.button('Recommend'):
#     recommendations = recommend(selected_movie_name)
#     for recommendation in recommendations:
#         st.write(recommendation)
#
# import pandas as pd
# import streamlit as st
# import pickle
# import requests
#
# # Load the movie dictionary and similarity matrix
# movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# # Convert movie_dict to DataFrame
# movies = pd.DataFrame(movie_dict)
#
# # Insert your TMDb API key here
# API_KEY = 'fede8f97352aa410a1f5b398837f3cc6'
#
# def fetch_poster(movie_id):
#     """Fetches the poster image URL for a given movie ID from TMDb."""
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         poster_path = data.get('poster_path')
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/w500{poster_path}"
#     return None
#
# def recommend(movie):
#     """Generates movie recommendations based on the selected movie."""
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id  # Ensure 'movie_id' column exists in the DataFrame
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_posters
#
# # Streamlit UI
# st.title('Movie Recommender System')
# selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)
#
# if st.button('Recommend'):
#     recommendations, posters = recommend(selected_movie_name)
#     for i in range(len(recommendations)):
#         st.write(recommendations[i])
#         if posters[i]:
#             st.image(posters[i], width=150)
#         else:
#             st.write("Poster not available.")

import pandas as pd
import streamlit as st
import pickle
import requests

# Load the movie dictionary and similarity matrix
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert movie_dict to DataFrame
movies = pd.DataFrame(movie_dict)

# Insert your TMDb API key here
API_KEY = 'fede8f97352aa410a1f5b398837f3cc6'


def fetch_poster(movie_id):
    """Fetches the poster image URL for a given movie ID from TMDb."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return None


def recommend(movie):
    """Generates movie recommendations based on the selected movie."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Ensure 'movie_id' column exists in the DataFrame
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


# Streamlit UI
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie_name)

    # Create columns for each recommendation
    cols = st.columns(len(recommendations))
    for idx, col in enumerate(cols):
        with col:
            st.text(recommendations[idx])  # Display movie title
            if posters[idx]:
                st.image(posters[idx], width=150)  # Display poster
            else:
                st.write("Poster not available.")

