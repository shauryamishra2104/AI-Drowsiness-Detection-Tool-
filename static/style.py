import streamlit as st


def load_home_css():
    st.markdown("""
    <style>

    /* Hide Top Bar of Streamlit */
                
        #MainMenu , footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top:1.5rem  !important;
            }

    /* Main background */
    .stApp {
        background: black;
        color: #38bdf8;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Main title */
    h1 {
        text-align: center;
        color: #00e5ff;
        font-size: 38px;
        font-weight: 700;
        text-shadow: 0px 0px 15px rgba(0,229,255,0.4);
        margin-bottom: 10px;
    }

    /* Description text */
    p {
        color: #FFFFFF;
        font-size: 50px;
    }

    /* Markdown container (box effect) */
    div[data-testid="stMarkdownContainer"] {
        background: rgba(255,255,255,0.03);
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.08);
        backdrop-filter: blur(8px);
    }

        /* Input container */
    div[data-baseweb="input"] {
        background-color: #000000 !important;
        border-radius: 10px;
        border: 1px solid #334155 !important;
    }

    /* Actual text box */
    div[data-baseweb="input"] input {
        background-color: #000000 !important;
        color: white !important;
        font-size: 18px !important;
    }

    /* Placeholder text */
    div[data-baseweb="input"] input::placeholder {
        color: #94a3b8 !important;
    }

    /* Label text */
    label {
        color: #38bdf8 !important;
        font-weight: 500;
        font-size:18px !important;
    }

    /* Button styling (Start Session) */
    button {
        background: linear-gradient(90deg, #00e5ff, #3b82f6) !important;
        color: black !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 2px 20px !important;
        border: none !important;
        transition: 0.3s ease-in-out;
    }

    button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 20px rgba(0,229,255,0.5);
    }

    /* Divider */
    hr {
        border: 1px solid #1f2937;
    }

    /* Bullet list styling */
    ul {
        color: #cbd5e1;
    }

    </style>
    """, unsafe_allow_html=True)


def load_detector_css():
    st.markdown("""
    <style>
    
    /* Hide Top Bar of Streamlit */
                
        #MainMenu , footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top:1.5rem  !important;
            }


    /* Whole page background */
    .stApp {
        background: linear-gradient(135deg, #0b1220, #111827);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Main title */
    h1 {
        text-align: center;
        color: #00e5ff;
        font-weight: 700;
        text-shadow: 0px 0px 10px rgba(0,229,255,0.4);
    }

    /* Subtitle / sections */
    h3 {
        color: #38bdf8;
        font-weight: 600;
    }

    /* Divider */
    hr {
        border: 1px solid #1f2937;
    }

    /* Webcam container (WebRTC box) */
    div[data-testid="stVerticalBlock"] {
        border-radius: 15px;
    }

    /* WebRTC video frame styling */
    video {
        border-radius: 15px;
        box-shadow: 0px 0px 25px rgba(0, 229, 255, 0.25);
        border: 2px solid rgba(0, 229, 255, 0.2);
    }



    /* Buttons (Logout) */
    button {
        margin-top: 100px;
        background: linear-gradient(90deg, #ef4444, #f97316) !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 5px 20px !important;
        border: none !important;
        transition: 0.3s ease-in-out;
    }

    button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 15px rgba(239, 68, 68, 0.6);
    }

    /* Camera section spacing */
    .stVideo {
        border-radius: 15px;
    }

    /* Info text */
    .stMarkdown {
        color: #cbd5e1;
    }

    </style>
    """, unsafe_allow_html=True)