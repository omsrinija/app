def get_wellness_tip(mood):
    tips = {
        "Positive": "😊 Keep up the great mood! Keep doing what you love.",
        "Neutral": "😐 Try some relaxation exercises or a short walk to boost your mood.",
        "Negative": "😔 Consider taking deep breaths, journaling your thoughts, or talking to someone you trust.",
    }
    return tips.get(mood, "💙 Take care of yourself today!")