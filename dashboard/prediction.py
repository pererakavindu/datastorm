import streamlit as st
import pandas as pd

def changeTargetColumn(row):
    if (row['target_column'] == 1):
        return 'False'
    elif (row['target_column'] == 0):
        return 'True'
    return 'Error'

st.markdown("# Prediction page")
st.sidebar.markdown("# Prediction page")

sampleDataFrame = pd.read_csv('sample_submission_storming_round.csv')

testDataFrame = pd.read_csv('test_storming_round.csv')

merged_df = pd.merge(sampleDataFrame, testDataFrame, on='row_id', how='inner')

merged_df['target_column'] = merged_df.apply(changeTargetColumn, axis=1)

# Select only the desired columns
selected_columns = ['agent_code', 'target_column']
final_df = merged_df[selected_columns]

# Optional: Rename columns for nicer display
final_df = final_df.rename(columns={
    'agent_code': 'Agent Code',
    'target_column': 'NIL Status In Next Month'
})

# Display with Streamlit
st.dataframe(final_df, use_container_width=True, height=600)