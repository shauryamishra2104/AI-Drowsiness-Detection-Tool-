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
        }
    )

    alarm_placeholder = st.empty()

    if ctx.video_processor:
        if ctx.video_processor.alarm_triggered:
            with open("alarm.mp3", "rb") as f:
                audio_bytes = f.read()

            b64 = base64.b64encode(audio_bytes).decode()

            alarm_placeholder.markdown(
                f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
            """
            <div style="
                border:6px dashed #444;
                border-radius: 0px;
                padding: 48px 32px;
                text-align: center;
                color: #888;
                margin-top: 32px;
            ">
                <h2 style="color:###ccc; margin-bottom:8px;">Keep face in front of Camera </h2>
                <p style="font-size:1.05rem;">
                    click <strong>Start</strong> to activate camera and AI Detector Tool
                </p>
            </div>
        """,unsafe_allow_html=True,
        )

    logout_button = st.button("Logout", key="logout button")
    if logout_button:
        st.session_state["login"] = "Home"
        st.rerun()

