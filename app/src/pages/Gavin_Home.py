import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')


# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Access List of Students Ready to Connect on Linkedin', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Student_Connect.py')

if st.button('Retrieve Total Number of Student Users',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/current_users.py')
  
if st.button('Reload a backup app into the log',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/logs_backup.py')

if st.button('Retrieve the last 10 submitted applications',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/recent_applications.py')

if st.button('Find all student IDs with a valid profile',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/student/id/profile.py')

if st.button('Get a count for the number of co-ops for each student',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/student/coop_count.py')

if st.button('Hire a new data analyst',
             type='primary',
             use_container_width=True):
    st.switch_page('pages/GHire_Analyst.py')