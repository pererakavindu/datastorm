import streamlit as st
import pandas as pd

st.markdown("# Classification page")
st.sidebar.markdown("# Classification page")

classificationDataFrame = pd.read_csv('selected_output.csv')

# Optional: Rename columns for nicer display
classificationDataFrame = classificationDataFrame.rename(columns={
    'agent_code': 'Agent Code',
    'performance': 'Performance'
})

# Display with Streamlit
st.dataframe(classificationDataFrame, use_container_width=True, height=600)