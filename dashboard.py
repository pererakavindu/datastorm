import streamlit as st
import pandas as pd

# Define the pages
prediction = st.Page("dashboard/prediction.py", title="Prediction")
classification = st.Page("dashboard/classication.py", title="Classification")
visualization = st.Page("dashboard/recommendation.py", title="Recommendation")

# Set up navigation
pg = st.navigation([prediction, classification, visualization])

# Run the selected page
pg.run()