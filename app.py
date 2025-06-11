import streamlit as st
from datetime import date
import pandas as pd
import os

# Import modules (make sure all these files exist and are implemented correctly)
from challenge_75hard import main as hard_75_main
from activities import self_care_activities_page
from habit_tracker import habit_tracker_page, load_habit_data
from journal import mood_journal_page
from mood_analysis import mood_analysis_and_tips_page
from suggestions import get_lifestyle_suggestion
# from wellness_tips import get_wellness_tip  # Uncomment if implemented

def main():
    st.set_page_config(page_title="SereneMind", layout="centered")
    st.title("🌟 SereneMind – AI Mood Journal + Wellness Coach")

    menu = [
        "Home",
        "Mood Analysis & Tips",
        "Self-Care Activities",
        "Habit Tracker",
        "75 Hard Challenge",
        "Lifestyle Suggestions",
        "Mood Journal",
        # "Wellness Tips",  # Uncomment if get_wellness_tip() is implemented
    ]

    choice = st.sidebar.selectbox("🧭 Navigation", menu)

    if choice == "Home":
        st.header("Welcome to SereneMind!")
        st.write("Your personal AI-powered mood journal and wellness coach.")
        st.write("Use the sidebar to navigate between features.")

    elif choice == "Mood Analysis & Tips":
        mood_analysis_and_tips_page()

    elif choice == "Self-Care Activities":
        self_care_activities_page()

    elif choice == "Habit Tracker":
        habit_tracker_page()

    elif choice == "75 Hard Challenge":
        hard_75_main()

    elif choice == "Lifestyle Suggestions":
        today = date.today().isoformat()
        df = load_habit_data()
        if not df.empty and "Date" in df.columns and today in df["Date"].values:
            today_row = df[df["Date"] == today].iloc[0]
            habits = today_row.to_dict()
            suggestions = get_lifestyle_suggestion(habits)
            st.header("🌿 Lifestyle Suggestions Based on Today's Habits")
            if suggestions:
                for tip in suggestions:
                    st.write(tip)
            else:
                st.success("🎉 Great job! You followed all healthy habits today!")
        else:
            st.warning("⚠️ You haven't logged any habits for today yet in the Habit Tracker.")

    elif choice == "Mood Journal":
        mood_journal_page()

    # elif choice == "Wellness Tips":
    #     get_wellness_tip()

if __name__ == "__main__":
    main()
