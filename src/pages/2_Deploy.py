"""Contains the `Deploy` page contents of the app."""
import streamlit as st

st.set_page_config(
    page_title="Deploy",
    page_icon="🚀️",
)


st.title("Deploy 🚀️")
st.divider()
st.markdown(
    """

1. Push local repo to GitHub.
2. Go to [Health Universe](https://www.healthuniverse.com).
3. Log in or create an account.
4. Click **Deploy App**.
5. Fill out fields.
6. Press **Deploy**. This process may take a few minutes.

Congratulations! Once you've completed these steps, your
Python model should be available as a Streamlit app on Health Universe!
"""
)
