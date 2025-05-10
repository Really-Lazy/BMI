import streamlit as st
import cv2
import numpy as np
from fer import FER

st.set_page_config(page_title="😡🤖😊 AI Emotion Detector", layout="centered")
st.title("🎥 AI Face Emotion Detector")

# Initialize emotion detector
detector = FER(mtcnn=True)

# Streamlit webcam checkbox
run = st.checkbox('Start Camera')

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    while run:
        ret, frame = cap.read()
        if not ret:
            st.warning("Failed to access camera.")
            break

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect emotions
        result = detector.detect_emotions(rgb_frame)
        
        # Draw results
        for face in result:
            (x, y, w, h) = face["box"]
            emotions = face["emotions"]
            max_emotion = max(emotions, key=emotions.get)
            max_score = emotions[max_emotion]

            # Draw face box
            cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Display top emotion + % on face
            cv2.putText(
                rgb_frame,
                f"{max_emotion}: {int(max_score * 100)}%",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 0, 0),
                2,
            )

            # Show mad and happy % specifically
            mad_pct = int(emotions["angry"] * 100)
            happy_pct = int(emotions["happy"] * 100)

            st.write(f"😡 Mad: {mad_pct}%   😊 Happy: {happy_pct}%")

        # Update Streamlit image
        FRAME_WINDOW.image(rgb_frame)

    cap.release()
