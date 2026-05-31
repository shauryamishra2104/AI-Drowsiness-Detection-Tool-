import streamlit as st
from streamlit_webrtc import webrtc_streamer,WebRtcMode
from detector.drowsiness import DrowsinessVideoProcessor
from static.style import load_detector_css



def detector_page():
    load_detector_css()
    username =st.session_state.get("username")
    st.title(f"Hii!! {username}")

    st.divider()

    st.write("### Live Camera Feed")
        
    webrtc_streamer(
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

