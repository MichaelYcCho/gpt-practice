import streamlit as st

st.selectbox(
    "Choose your model",
    (
        "GPT-3",
        "GPT-4",
    ),
)

st.subheader("Welcome to Streamlit!")

st.markdown(
    """
    #### I love it!
"""
)
