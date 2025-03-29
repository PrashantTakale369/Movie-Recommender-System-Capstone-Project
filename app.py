from idlelib.format import reformat_comment

import streamlit as st
import pickle
import pandas as pd
import requests


# This is the Code where we are calling the API
def fetch_poster(movie_id):
    responce = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2f0d0db82da86c0e17ebe3b9d7ca3773&language=en-US'.format(movie_id))
    # For movies
    data = responce.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# This is the ( Main Function ) where we are used All the code logic
def Recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:10]

    recommended_movies = []  # this is the list where all the Sameilar Movies Store
    recommended_movies_poster = [] # this is the list where all the movuies fetch poster store whic is
    # we are fetching from the API through so when we  recommand the movies then it will show the image .

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id # here we are storing the all the mvies id so we can give this for fetching poster
        # /// -----> Fetch Poster form API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


# importing the 5000 movies data on our web by usig pickle methods
movies_dict  = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

# Creating the box to search the all the movies

selected_movie_name = st.selectbox("which type of movie you want to Watch : ?",movies['title'].values)

# ctrating the buttons to

if st.button(" Recommend "):
    names,poster = Recommend(selected_movie_name)


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
