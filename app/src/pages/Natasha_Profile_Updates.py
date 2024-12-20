import streamlit as st
import requests

st.title("Create and Update Profile")
option = st.radio("What would you like to do?", ["Create Profile", "Change Connect Preferences"])

# Create Profile
if option == "Create Profile":
    st.header("Create Profile")
    username = st.text_input("Username: ")
    profileType = st.text_input("What is your Co-op Status?") 
    connectButton = st.radio("You are Open to Connect with other students:", (True, False))

    if st.button("Create Profile"):
        if username and profileType:
            data = {
                "username": username,
                "profileType": profileType,
                "openToConnect": connectButton
            }
            response = requests.post(f"http://web-api:4000/student", json=data)
            if response.status_code == 200:
                st.success("Profile created successfully!")
            else:
                st.error(f"Failed to create profile. HTTP Status: {response.status_code}")
        else:
            st.warning("Please fill all fields!")

# Update whether user is open to connect in profile
elif option == "Change Connect Preferences":
    st.header("Change Your Connection Preferences")

    st_id = st.text_input("Student ID: ")
    connectButton = st.radio("You are open to connect:", (True, False))

    if st.button("Update Profile"):
        if st_id and connectButton is not None:
            data = {
                "openToConnect": connectButton
            }
            response = requests.put(f"http://web-api:4000/student/{st_id}", json=data)
            if response.status_code == 200:
                st.success("Preferences updated successfully!")
            else:
                st.error(f"Failed to update preferences. HTTP Status: {response.status_code}")