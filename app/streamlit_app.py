import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium
from pathlib import Path

st.set_page_config(page_title="Freshwater Stress Predictor", layout="wide")

def main():
    st.title("🌊 Freshwater Resource & Stress Predictor")
    st.caption("Predicting variations in freshwater availability and stress across global basins.")
    st.info("Data and model not loaded yet — complete Phases 1-5 first!")

if __name__ == "__main__":
    main()
