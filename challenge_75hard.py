import streamlit as st
import pandas as pd
import os
from datetime import date

FILE = "75hard_data.csv"

COLUMNS = [
    "Date",
    "Followed diet strictly (no cheat meals, no alcohol)",
    "Completed 1st workout (45 mins)",
    "Completed 2nd workout outside (45 mins)",
    "Drank 1 gallon of water",
    "Read 10 pages of nonfiction book",
    "Took progress photo"
]

def load_data():
    if os.path.exists(FILE):
        df = pd.read_csv(FILE)
        for col in COLUMNS[1:]:
            if col in df.columns:
                df[col] = df[col].astype(bool)
        # Keep only desired columns
        df = df[COLUMNS] if set(COLUMNS).issubset(df.columns) else pd.DataFrame(columns=COLUMNS)
    else:
        df = pd.DataFrame(columns=COLUMNS)
    return df

def save_data(df):
    df.to_csv(FILE, index=False)

def main():
    st.title("💪 75 Hard Challenge Tracker")

    df = load_data()
    today = date.today().isoformat()

    st.header(f"Track progress for: {today}")

    if today in df["Date"].values:
        row = df[df["Date"] == today].iloc[0]
        st.info("You already logged today's progress. You can update it below.")
    else:
        row = pd.Series({col: False for col in COLUMNS[1:]})

    values = {}
    for col in COLUMNS[1:]:
        values[col] = st.checkbox(col, value=row.get(col, False))

    if st.button("Save Today's Progress"):
        new_entry = {"Date": today, **values}
        df = df[df["Date"] != today]
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        save_data(df)
        st.success("✅ Today's progress saved!")

    if not df.empty:
        st.header("📊 Your 75 Hard Progress Summary")
        st.dataframe(df.sort_values("Date", ascending=False).set_index("Date"))