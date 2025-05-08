import streamlit as st
import pandas as pd

dataFrame = pd.read_csv('test_storming_round.csv')

st.title('Agent performance dashboard')

st.line_chart(dataFrame.groupby('agent_code')['net_income'].sum())