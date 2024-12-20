import streamlit as st
import requests

st.title("Edit Your Review")

option = st.radio("What would you like to do?", ["Update Review", "Delete Review"])

# Update Existing Review 
if option == "Update Review":
    st.header("Update an Existing Review")
    review_id = st.text_input("Review ID")
    rating = st.slider("New Rating (1-5)", 1, 5, 3)
    review_text = st.text_area("Update your review")

    if st.button("Update Review"):
        if review_id:
            data = {
                "rating": rating,
                "review_text": review_text
            }
            response = requests.put(f"http://web-api:4000/review/{review_id}", json=data)
            if response.status_code == 200:
                st.success("Review updated successfully!")
            else:
                st.error(f"Failed to update review. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")

elif option == "Delete Review":
    st.header("Delete Review")
    id = st.text_input("Review ID", key="remove_review_id")

    if st.button("Delete Review"):
        if id:
            data = {
                "review_id": id
            }
            response = requests.delete(f"http://web-api:4000/review/{id}", json=data)
            if response.status_code == 200:
                st.success("Review removed from user's profile successfully!")
            else:
                st.error(f"Failed to remove review. HTTP Status: {response.status_code}")
        else:
            st.warning("Please provide both Review ID!")
