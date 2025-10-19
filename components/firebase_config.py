import streamlit as st

firebaseConfig = {
    "apiKey": "AIzaSyCAgDpTsp4XUCyWwsQ-BKq35eWd3LiajWk",
    "authDomain": "earthscape-auth-5501a.firebaseapp.com",
    "databaseURL": "https://earthscape-auth-5501a-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "earthscape-auth-5501a",
    "storageBucket": "earthscape-auth-5501a.firebasestorage.app",
    "messagingSenderId": "981413608442",
    "appId": "1:981413608442:web:3a27f181f0ed650ef6c243"
}

firebase = st(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
