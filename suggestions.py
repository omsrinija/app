import streamlit as st

def get_lifestyle_suggestion(habits):
    suggestions = []

    if not habits.get("Wake up early", False):
        suggestions.append("🌅 Try waking up earlier to start your day fresh.")
    if not habits.get("Drink 8 glasses of water", False):
        suggestions.append("💧 Increase your water intake to stay hydrated.")
    if not habits.get("Exercise for 30 mins", False):
        suggestions.append("🏃 Add at least 30 minutes of exercise daily.")
    if not habits.get("Read for 20 mins", False):
        suggestions.append("📚 Spend some time reading to stimulate your mind.")
    if not habits.get("Meditate", False):
        suggestions.append("🧘 Practice meditation for mental clarity and relaxation.")
    if not habits.get("No junk food", False):
        suggestions.append("🍔 Avoid junk food to improve overall health.")
    if not habits.get("Sleep 7-8 hours", False):
        suggestions.append("🛌 Ensure you get 7-8 hours of quality sleep.")
    if not habits.get("Limit screen time before bed", False):
        suggestions.append("📵 Reduce screen time before sleeping for better rest.")
    if not habits.get("Eat fruits and vegetables", False):
        suggestions.append("🍎 Eat more fruits and vegetables daily.")
    if not habits.get("Take breaks during work/study", False):
        suggestions.append("⏸️ Take short breaks during work or study to refresh.")
    if not habits.get("Practice gratitude", False):
        suggestions.append("🙏 Practice gratitude to boost positivity.")
    if not habits.get("Maintain social connections", False):
        suggestions.append("👥 Stay connected with friends and family.")
    if not habits.get("Set daily goals", False):
        suggestions.append("🎯 Set clear daily goals to stay focused.")

    return suggestions