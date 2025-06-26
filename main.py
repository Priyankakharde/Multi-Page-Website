import streamlit as st
import firebase_admin

from firebase_admin import credentials 
from firebase_admin import auth

from streamlit_option_menu import option_menu


import about, account, home, trending, your_posts

st.set_page_config(
    page_title="Pondering",
)

class MultiApp:
    
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": function
        })    
        
    def run():
        
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Home','Account','Trending','Your Posts','About'],
                icons=['house-fill','person-circle','trophy-fill','file-text','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#050505"},
                    "icon": {"color": "#0a0909"},
                    "nav-link": {"font-size": "12px", "text-align": "left", "margin": "0"},
                    "nav-link-selected": {"background-color": "#ff0099"},}
    
            )
            
     
        if app == 'Home':
                home.app()
        if app == 'Account':
            account.app()       
        if app == 'Trending':
            trending.app()      
        if app == 'Your Posts':
            your_posts.app()
        if app == 'About':
            about.app()
                                    
    run()            
                
                            
            
            
