import streamlit as st

# Page Config
st.set_page_config(page_title="My Valentine", page_icon="❤️")

# Custom CSS for the "Alive" feel
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@300&display=swap');

    .stApp {
        background: linear-gradient(to bottom, #ffdde1, #ee9ca7);
    }

    .heart-main {
        font-size: 120px;
        text-align: center;
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.15); }
        100% { transform: scale(1); }
    }

    .title {
        font-family: 'Great Vibes', cursive;
        font-size: 80px;
        color: #d00000;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .message {
        font-family: 'Montserrat', sans-serif;
        font-size: 22px;
        color: #444;
        text-align: center;
        padding: 20px;
    }
    </style>
    
    <div class="heart-main">💖</div>
    <h1 class="title">For You, Always</h1>
    <p class="message">
        You make the world brighter just by being in it.<br>
        I wanted to code something as beautiful as your smile.
    </p>
    """, unsafe_allow_html=True)

if st.button("Click for a Surprise"):
    st.balloons()
    st.snow()
    st.markdown("<h2 style='text-align:center; color:#d00000; font-family:Great Vibes;'>I Love You!</h2>", unsafe_allow_html=True)
