import streamlit as st
import pandas as pd
from recommender import recommend

st.set_page_config(page_title="SHL AI Assessment Recommender")

st.title("SHL AI Assessment Recommender")
st.write("Enter a job requirement and get recommended SHL assessments.")

query = st.text_area("Job Requirement")

if st.button("Get Recommendations"):
    if query.strip() == "":
        st.warning("Please enter a job requirement.")
    else:
        df = recommend(query)

        if "Assessment Name" in df.columns and "Assessment_url" in df.columns:
            df["Assessment Link"] = df["Assessment_url"].apply(
                lambda x: f'<a href="{x}" target="_blank">Open Assessment</a>'
            )

            final_df = df[["Assessment Name", "Assessment Link"]]

            st.write(
                final_df.to_html(escape=False, index=False),
                unsafe_allow_html=True
            )
        else:
            st.error("Expected columns not found in dataset.")
