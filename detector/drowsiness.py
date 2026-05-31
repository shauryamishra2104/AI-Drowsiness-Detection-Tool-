import mediapipe as mp
import numpy as np
from streamlit_webrtc import VideoProcessorBase
import streamlit as st
import cv2
import av
from detector.process import calculation as calc


LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH_INDICES = [78, 308, 13, 14]
EAR_THRESHOLD = 0.25
EAR_CONSECUTIVE_FRAMES = 22
MAR_THRESHOLD = 0.6
MAR_CONSECUTIVE_FRAMES = 30


class DrowsinessVideoProcessor(VideoProcessorBase):
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.sleep_counter = 0
        self.yawn_counter = 0
        # self.alarm_triggered = False
        
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        h, w, _ = img.shape
        
        rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                left_eye_pts = np.array([[face_landmarks.landmark[i].x * w, face_landmarks.landmark[i].y * h] for i in LEFT_EYE])
                right_eye_pts = np.array([[face_landmarks.landmark[i].x * w, face_landmarks.landmark[i].y * h] for i in RIGHT_EYE])
                
                mouth_pts = {}
                for i in MOUTH_INDICES:
                    mouth_pts[i] = np.array([face_landmarks.landmark[i].x * w, face_landmarks.landmark[i].y * h])

                left_ear =  calc.calculate_ear(left_eye_pts)
                right_ear = calc.calculate_ear(right_eye_pts)
                avg_ear = (left_ear + right_ear) / 2.0
                
                mar = calc.calculate_mar(mouth_pts)

                if avg_ear < EAR_THRESHOLD:
                    self.sleep_counter += 1
                else:
                    self.sleep_counter = 0
                    # self.alarm_triggered = False
                
                if self.sleep_counter >= EAR_CONSECUTIVE_FRAMES:
                    cv2.putText(img, "DROWSINESS DETECTED!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    # self.alarm_triggered = True

                if mar > MAR_THRESHOLD:
                    self.yawn_counter += 1
                else:
                    self.yawn_counter = 0
                    
                if self.yawn_counter > MAR_CONSECUTIVE_FRAMES:
                    cv2.putText(img, "YAWNING WARNING!", (50, 100), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 3)
                   
                # if self.yawn_counter == MAR_CONSECUTIVE_FRAMES:
                #     self.alarm_triggered = True
                
                cv2.putText(img, f"EAR: {avg_ear:.2f}", (w - 150, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(img, f"MAR: {mar:.2f}", (w - 150, 60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        
        return av.VideoFrame.from_ndarray(img, format="bgr24")
