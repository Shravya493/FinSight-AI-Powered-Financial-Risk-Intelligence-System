from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(df):
    analyzer = SentimentIntensityAnalyzer()

    df["Sentiment"] = df["News"].apply(
        lambda x: analyzer.polarity_scores(str(x))["compound"]
    )

    market_score = df["Sentiment"].mean()

    return market_score, df