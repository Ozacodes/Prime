import streamlit as st

# URL to redirect to
redirect_url = "http://prime-bca-prep-9d4b2kn.gamma.site"

# Streamlit page configuration
st.set_page_config(page_title="Redirect Page", layout="centered")

# JavaScript for redirection
st.markdown(f"""
    <meta http-equiv="refresh" content="0; url={redirect_url}">
    <a href="{redirect_url}">Click here if you are not redirected</a>
""", unsafe_allow_html=True)

# Optional: Display a message before redirection
st.write("You are being redirected to the new website.")
