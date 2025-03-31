from transformers import pipeline

def analyze_sentiment(text):
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(text)
    return result[0]

if __name__ == "__main__":
    sample_text = "Apple's stock is soaring due to great earnings report!"
    sentiment = analyze_sentiment(sample_text)
    print(f"Sentiment: {sentiment}")