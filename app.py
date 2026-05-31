import streamlit as st
from detector.detector_page import detector_page
from static.style import load_home_css


st.set_page_config(
    page_title="Drowsiness Detection Tool",
    page_icon=r"C:\Users\shaurya mishra\Drowsiness Detection Tool\static\gemini-svg.svg",
    layout="centered"
    )   

def home_page():

    load_home_css()
    st.title("🤖 AI Real-Time Drowsiness Detection Tool with Alarm system")

    if "username" not in st.session_state:
        st.session_state["username"] = ""
    
    st.markdown("")
    st.markdown("")

    st.markdown("""
                This application uses computer vision to track your eye and mouth movements in real-time. 
                * **EAR (Eye Aspect Ratio):** Drops when eyes close. Triggers a **Drowsiness Alarm**.
                * **MAR (Mouth Aspect Ratio):** Spikes when the mouth opens wide. Triggers a **Yawn Warning**.
                """)

    st.divider()
    
    st.markdown(" Welcome !  Please enter a username to start")
    username = st.text_input("Name (unique)", placeholder="unique name e.g shauryamishra")

    if username:
        st.session_state["username"] = username

    submit_button = st.button("Start Session",key="start button")
    
    if submit_button:
        st.session_state["login"] = "Detector"
        st.rerun()

def main():
    if "login" not in st.session_state:
        st.session_state["login"] = "Home"

    if st.session_state["login"] == "Home":
        home_page()
        return

    if st.session_state["login"] == "Detector":
        detector_page()


main()

