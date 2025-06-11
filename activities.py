import streamlit as st
import random

def self_care_activities_page():
    st.header("💆‍♀️ Self-Care Activities")
    st.caption("Explore calming activities to improve your mood and mental well-being.")

    # Daily Quote with session persistence
    quotes = [
        "Keep your face always toward the sunshine—and shadows will fall behind you.",
        "The only way to do great work is to love what you do.",
        "Believe you can and you're halfway there.",
        "Do something today that your future self will thank you for.",
    ]
    if "daily_quote" not in st.session_state:
        st.session_state.daily_quote = random.choice(quotes)
    st.markdown(f"💬 **Quote of the Day:** *{st.session_state.daily_quote}*")

    # Breathing Exercise
    with st.expander("🌬️ Breathing Exercise"):
        st.write("Practice the 4-7-8 breathing method to relax:")
        st.write("1. Breathe in deeply for **4 seconds**.")
        st.write("2. Hold your breath for **7 seconds**.")
        st.write("3. Exhale slowly for **8 seconds**.")
        st.write("🔁 Repeat this cycle **3 times**.")

    # Music Therapy
    with st.expander("🎵 Music Therapy"):
        st.write("Listening to music can improve your mood and reduce stress.")
        st.write("🎧 Try playing your favorite uplifting song now!")

    # Doodle Pad (Placeholder)
    with st.expander("🎨 Doodle Pad"):
        st.write("🖌️ Imagine a blank canvas here for doodling.")
        st.write("Try drawing on paper and relaxing your mind!")
        st.write("_(Tip: Use the Streamlit drawable canvas for future enhancement.)_")

    # Virtual Walk
    with st.expander("🚶 Virtual Walk"):
        st.write("Take a moment to stand up and walk around your room or outside.")
        st.write("🚶‍♂️ Feel the fresh air and clear your mind.")

    # Random Self-Care Challenge
    challenges = [
        "Drink a glass of water right now.",
        "Take 5 deep breaths.",
        "Write down 3 things you like about yourself.",
        "Stretch your arms and legs for 2 minutes.",
        "Smile for 30 seconds in front of a mirror.",
    ]
    st.markdown("---")
    st.markdown(f"🌟 **Random Self-care Challenge:** *{random.choice(challenges)}*")
