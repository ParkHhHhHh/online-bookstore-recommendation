import streamlit as st
import requests

st.title("📚 Online Bookstore Recommendation System")

user_id = st.number_input("Enter your user ID", min_value=1)

if st.button("Get Recommendations"):
    response = requests.post("http://localhost:8000/recommend",
                             json={"user_id": user_id})
    st.write("### Recommended Books:")
    st.json(response.json())
