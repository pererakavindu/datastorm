import streamlit as st
import pandas as pd

def recommendIntervention(category):
    status = 'Error'
    if (category == 'High'):
        status = 'Offer leadership role, incentives or referrals'
    elif (category == 'Medium'):
        status = 'Provide mentorship, skill-building workshops'
    else:
        status = 'Assign training, monitor closely, motivational sessions'

    return status

st.markdown("# Recommendation page")
st.sidebar.markdown("# Recommendation page")

recommendationDataFrame = pd.read_csv('selected_output.csv')

recommendationDataFrame['recommendation'] = (
    recommendationDataFrame['performance']
    .apply(recommendIntervention)
)

# Optional: Rename columns for nicer display
recommendationDataFrame = recommendationDataFrame[['agent_code', 'recommendation']].rename(columns={
    'agent_code': 'Agent Code',
    'recommendation': 'Recommendation'
})

# Display with Streamlit
st.dataframe(recommendationDataFrame, use_container_width=True, height=600)