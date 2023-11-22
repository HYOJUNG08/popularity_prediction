import streamlit as st
from streamlit_extras.let_it_rain import rain 
import time
from streamlit import session_state as state
from spotify import Spotify
import random
import joblib
from category_encoders import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
import pandas as pd

def loading():
    rain(
        emoji="😭",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

def get_predictions(data):
    model_path = Path(__file__).parent
    model_path = model_path/'nonscale_model.pkl'
    model = joblib.load(model_path)
    predictions = model.predict(data)
    return predictions

def main():
    st.title("Predict Your Song")

    artist_name = st.text_input("🎤 Artist")
    song_title = st.text_input("🎶 Track Name")
        
    if st.button("Popularity Prediction"):
        #난수 생성
        random_value = random.choice([0, 1])
        if random_value >= 0.5:
            
            #객체 생성
            s = Spotify(artist_name,song_title)
            print(s.artist)
            print(s.track)  

            with st.spinner('Wait for it...'):
                #예측값 받아오기

                pred = get_predictions(data)
                time.sleep(5)
            st.success(f"Prediction for Artist: {artist_name}, Track Name: {song_title}, Prediction: {pred}")
        else:
            loading()
            st.error("Oops! Something went wrong.")

if __name__ == "__main__":
    main()