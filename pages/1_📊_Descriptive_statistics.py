import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

st.set_page_config(page_title="Recommender system", page_icon="📊")

st.title("Mushroom Recommender System")
st.markdown("""
            This page lets you choose the characteristics of a mushroom within our database and returns the 5 most similar mushrooms to it.
            Further this page shows some statistical visualisations based on the group of mushrooms that are most similar to the one you chose.
            """)

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
