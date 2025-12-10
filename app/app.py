import streamlit as st
import requests

# Set page title and description
st.set_page_config(page_title="Online Bookstore Recommendations", layout="wide")
st.title("📚 Book Recommendations")
st.markdown("Welcome to the Online Bookstore! Get personalized book recommendations based on your preferences.")

# Get user input for user_id
user_id = st.number_input("Enter your user ID", min_value=1, step=1)

# Function to get recommendations from the FastAPI backend
def get_recommendations(user_id):
    url = "http://localhost:8000/recommend"
    response = requests.post(url, json={"user_id": user_id})
    return response.json()

# Display button and recommendations
if st.button("Get Recommendations"):
    recommendations = get_recommendations(user_id)
    if "recommended_books" in recommendations:
        st.write("### Recommended Books:")
        st.write(", ".join([str(book_id) for book_id in recommendations["recommended_books"]]))
    else:
        st.error("Error fetching recommendations. Please try again.")
))
