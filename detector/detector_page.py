import streamlit as st
from streamlit_webrtc import webrtc_streamer,WebRtcMode,RTCConfiguration
from detector.drowsiness import DrowsinessVideoProcessor
from static.style import load_detector_css



RTC_CONFIG = {
    "iceServers": [
        {
            "urls": ["turn:openrelay.metered.ca:443?transport=tcp"],
            "username": "openrelayproject",
            "credential": "openrelayproject",
        }
    ]
}


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
        rtc_configuration=RTC_CONFIG,
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

    logout_button = st.button("Logout", key="logout button")
    if logout_button:
        st.session_state["login"] = "Home"
        st.rerun()

