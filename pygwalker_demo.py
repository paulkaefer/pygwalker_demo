from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st

# Streamlit page configuration:
st.set_page_config(
  page_title="Playing with PyGWalker in a basic Streamlit app",
  layout="wide"
)

# Import your data
# originally from https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv
df = pd.read_csv("bike_sharing_dc.csv")

pyg_app = StreamlitRenderer(df)

pyg_app.explorer()
