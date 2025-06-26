
import streamlit as  st

def app():
    
    st.title('Welcome to :violet[pondering]')
    
    choice = st.selectbox('login/signup', ['login', 'signup'])
    if choice == 'login':
        
        email=st.text_input('Email Address')
        password=st.text_input('Password', type='password')
        
        st.button('Login')
        
    else:
        
        email=st.text_input('Email Address')
        password=st.text_input('Password', type='password')
        
        st.button('Login')
        
        st.write('signup')