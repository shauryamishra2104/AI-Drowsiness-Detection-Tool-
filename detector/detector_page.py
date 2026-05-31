import streamlit as st
from streamlit_webrtc import webrtc_streamer,WebRtcMode
from detector.drowsiness import DrowsinessVideoProcessor
from static.style import load_detector_css
import base64
import time


def detector_page():
    load_detector_css()
    username =st.session_state.get("username")
    st.title(f"Hii!! {username}")

    st.divider()

    st.write("### Live Camera Feed")
        
    context = webrtc_streamer(
        key="Drowsiness-detection",
        video_processor_factory=DrowsinessVideoProcessor,
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={
            "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
        },
            media_stream_constraints={
            "video": True,
            "audio":False,
        },
        async_processing=True,
    )

    st.markdown(
        """
        <div style="
            border: 6px dashed #444;
            padding: 48px 32px;
            text-align: center;
            color: #888;
            margin-top: 32px;
        ">
            <h2 style="color:#ccc; margin-bottom:8px;">
                Keep Face In Front Of Camera
            </h2>
            <p style="font-size:1.05rem;">
                Click <strong>START</strong> to activate camera and AI Detector Tool
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    if context.video_processor:

        if context.video_processor.alarm_triggered:

            st.error("🚨 Drowsiness / Yawning Detected!")

            st.audio("alarm.mp3")

    logout_button = st.button("Logout", key="logout button")
    if logout_button:
        st.session_state["login"] = "Home"
        st.rerun()

