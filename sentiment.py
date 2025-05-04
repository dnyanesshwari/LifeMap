from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score < -0.3:
        return "😢", "Sad"
    elif score < 0.1:
        return "😐", "Neutral"
    elif score < 0.5:
        return "🙂", "Happy"
    else:
        return "🤩", "Excited"
