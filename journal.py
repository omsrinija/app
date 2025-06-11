import streamlit as st
from datetime import date
import pandas as pd
import os

JOURNAL_FILE = "journal.csv"

# Load journal data safely
def load_journal():
    if not os.path.exists(JOURNAL_FILE) or os.path.getsize(JOURNAL_FILE) == 0:
        return pd.DataFrame(columns=["Date", "Entry"])
    try:
        return pd.read_csv(JOURNAL_FILE)
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Date", "Entry"])

# Save or update entry for a specific date
def save_entry(entry_date, entry_text):
    df = load_journal()
    # Remove existing entry for the same date
    df = df[df["Date"] != entry_date]
    new_entry = pd.DataFrame([[entry_date, entry_text]], columns=["Date", "Entry"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(JOURNAL_FILE, index=False)

# Main Streamlit page
def mood_journal_page():
    st.title("📝 Mood Journal")

    today = date.today().isoformat()
    st.markdown(f"### Today's Date: `{today}`")

    journal_text = st.text_area("Write about your day, your mood, thoughts or reflections:")

    if st.button("Save Entry"):
        if journal_text.strip() != "":
            save_entry(today, journal_text.strip())
            st.success("✅ Your journal entry has been saved!")
        else:
            st.warning("⚠️ Entry is empty. Please write something before saving.")

    with st.expander("📖 View Past Journal Entries"):
        df = load_journal()
        if not df.empty:
            df_sorted = df.sort_values("Date", ascending=False)
            for _, row in df_sorted.iterrows():
                st.markdown(f"**📅 {row['Date']}**")
                st.text(row["Entry"])  # Preserves line breaks
                st.markdown("---")
        else:
            st.info("No journal entries yet.")
