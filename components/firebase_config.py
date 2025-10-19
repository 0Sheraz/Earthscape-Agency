import streamlit as st

class DemoAuth:
    def sign_in_with_email_and_password(self, email, password):
        return {"idToken": "demo-token", "localId": "demo-user", "email": email}
    
    def create_user_with_email_and_password(self, email, password):
        return {"idToken": "demo-token", "localId": "demo-user", "email": email}

auth = DemoAuth()
