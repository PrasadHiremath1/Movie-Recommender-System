import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selectedMovie = st.selectbox('select movie name', movies['title'].values)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=e40f781e600f9f51d8364eb7b14d5a4d&language=en-US'.format(movie_id))
    data = response.json()
    return 'http://image.tmdb.org/t/p/w500/' + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        #     fetch posters
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


if st.button('Recommend'):
    names, posters = recommend(selectedMovie)  # Function should return lists of names and poster URLs

    # Create 5 equal columns
    cols = st.columns(5)

    # Loop through each column and display movie details
    for i in range(5):
        with cols[i]:
            # Title inside a fixed-height div (40px) with centered text
            st.markdown(
                f"""
                <div style="height: 50px; text-align: center; 
                            font-size: 14px; font-weight: bold; 
                            display: flex; align-items: center; 
                            justify-content: center; overflow: hidden;">
                    {names[i]}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Poster below the title
            st.image(posters[i], use_container_width=True)
