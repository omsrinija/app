import streamlit as st
import pandas as pd

def analyze_mood(text):
    positive_words = ['happy', 'good', 'great', 'fantastic', 'joy', 'love', 'excited', 'calm', 'peaceful', 'relaxed']
    negative_words = ['sad', 'bad', 'terrible', 'hate', 'angry', 'upset', 'anxious', 'stressed', 'depressed', 'worried']

    text_lower = text.lower()
    score = 0

    for word in positive_words:
        if word in text_lower:
            score += 1

    for word in negative_words:
        if word in text_lower:
            score -= 1

    if score > 0:
        return "Positive", score
    elif score < 0:
        return "Negative", score
    else:
        return "Neutral", score

def get_wellness_tips(mood):
    if mood == "Positive":
        tips = [
            "Keep up the good vibes! Practice gratitude daily.",
            "Share your happiness with friends or family.",
            "Try some light exercise like yoga or walking.",
            "Maintain a balanced diet to support your energy."
        ]
        activities = ["Meditation", "Journaling about things you love", "Listening to uplifting music", "Going for a nature walk"]
    elif mood == "Negative":
        tips = [
            "Take deep breaths to calm your mind.",
            "Reach out and talk to someone you trust.",
            "Try to get some restful sleep tonight.",
            "Avoid negative news or social media for a while."
        ]
        activities = ["Mindfulness meditation", "Writing down your thoughts", "Doing a creative hobby", "Gentle stretching or yoga"]
    else:
        tips = [
            "Check in with yourself regularly.",
            "Balance work and relaxation.",
            "Stay hydrated and eat healthy.",
            "Set small goals to boost your mood."
        ]
        activities = ["Light exercise", "Reading a favorite book", "Listening to calming music", "Taking breaks throughout the day"]
    return tips, activities

def mood_to_numeric(mood):
    if mood == "Positive":
        return 1
    elif mood == "Negative":
        return -1
    else:
        return 0

def mood_analysis_and_tips_page():
    st.title("🧠 Mood Analysis & Wellness Tips")

    user_input = st.text_area("💬 How are you feeling today? Share your thoughts:")

    if 'mood_history' not in st.session_state:
        st.session_state.mood_history = []

    if st.button("Analyze Mood"):
        if user_input.strip():
            mood, score = analyze_mood(user_input)

            st.session_state.mood_history.append({
                "text": user_input,
                "mood": mood,
                "score": mood_to_numeric(mood)
            })

            color = {"Positive": "#4CAF50", "Negative": "#F44336", "Neutral": "#FFC107"}[mood]
            emoji = {"Positive": "😊", "Negative": "😞", "Neutral": "😐"}[mood]

            st.markdown(f"<h2 style='color:{color};'>Your mood is: {mood} {emoji}</h2>", unsafe_allow_html=True)

            tips, activities = get_wellness_tips(mood)

            with st.expander("💡 Wellness Tips"):
                for tip in tips:
                    st.write(f"• {tip}")

            with st.expander("🎯 Suggested Activities"):
                for act in activities:
                    st.write(f"• {act}")
        else:
            st.warning("⚠️ Please write something to analyze.")

    if st.session_state.mood_history:
        st.markdown("---")
        st.subheader("📈 Mood History")

        df = pd.DataFrame(st.session_state.mood_history)
        df.index = pd.to_datetime(pd.Series(range(len(df))), unit='D', origin=pd.Timestamp.today())
        st.line_chart(df['score'])

        with st.expander("📝 Recent Mood Entries"):
            for i, entry in enumerate(reversed(st.session_state.mood_history[-5:]), 1):
                st.write(f"{i}. Mood: **{entry['mood']}** — Text: {entry['text'][:100]}{'...' if len(entry['text']) > 100 else ''}")
