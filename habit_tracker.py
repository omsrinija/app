import streamlit as st
import pandas as pd
from datetime import date
import os

HABITS = [
    "Wake up early",
    "Drink 8 glasses of water",
    "Exercise for 30 mins",
    "Read for 20 mins",
    "Meditate",
    "No junk food",
    "Sleep 7-8 hours",
    "Limit screen time before bed",
    "Eat fruits and vegetables",
    "Take breaks during work/study",
    "Practice gratitude",
    "Maintain social connections",
    "Set daily goals",
]

CSV_FILE = "habit_log.csv"

def load_habit_data():
    if os.path.exists(CSV_FILE):
        try:
            df = pd.read_csv(CSV_FILE)
            # Ensure all expected columns are present
            for habit in HABITS:
                if habit not in df.columns:
                    df[habit] = False
            if "Date" not in df.columns:
                df["Date"] = ""
            return df[["Date"] + HABITS]
        except Exception:
            return pd.DataFrame(columns=["Date"] + HABITS)
    else:
        return pd.DataFrame(columns=["Date"] + HABITS)

def save_habit_data(data):
    data.to_csv(CSV_FILE, index=False)

def habit_tracker_page():
    st.title("✅ Daily Habit Tracker")

    today = date.today().isoformat()
    df = load_habit_data()

    st.markdown(f"### Habits for Today – `{today}`")

    if today in df["Date"].values:
        st.success("✅ You've already logged today's habits!")
        today_data = df[df["Date"] == today]
        for habit in HABITS:
            df[habit] = df[habit].astype(bool)
        completed = today_data[HABITS].sum(axis=1).values[0]
        st.metric("Habits Completed Today", f"{int(completed)} / {len(HABITS)}")
        st.dataframe(today_data.set_index("Date"))
    else:
        status = {}
        cols = st.columns(2)
        for i, habit in enumerate(HABITS):
            status[habit] = cols[i % 2].checkbox(habit)

        if st.button("Save Today's Habits"):
            new_row = {"Date": today}
            new_row.update(status)
            df = pd.concat([df[df["Date"] != today], pd.DataFrame([new_row])], ignore_index=True)
            save_habit_data(df)
            st.success("✅ Habits saved successfully!")
            st.dataframe(pd.DataFrame([new_row]).set_index("Date"))

    with st.expander("📊 View Full Habit History"):
        if not df.empty:
            df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
            df = df.sort_values("Date", ascending=False)
            st.dataframe(df.set_index("Date"))
        else:
            st.info("No data logged yet.")
