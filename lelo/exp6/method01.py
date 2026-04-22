# Method 1: Using Positive and Negative Word Count – With Normalization for Calculating Sentiment Score

import pandas as pd
import re
from collections import Counter



def load_words(filepath):
   with open(filepath, "r") as f:
       return set(word.strip().lower() for word in f.read().split(","))


def rating_to_label(r):
   r = float(r)
   if r >= 4:
       return "Positive"
   if r <= 2:
       return "Negative"
   return "Neutral"


def preprocess(text: str) -> list:
   text = re.sub(r"[^a-z\s]", "", str(text).lower())
   return text.split()


def sentiment_score(tokens: list, positive_words: set, negative_words: set) -> float:
   if not tokens:
       return 0.0
   pos = sum(1 for t in tokens if t in positive_words)
   neg = sum(1 for t in tokens if t in negative_words)
   return round((pos - neg) / len(tokens), 6)


def classify(score: float) -> str:
   if score > 0:
       return "Positive"
   if score < 0:
       return "Negative"
   return "Neutral"


POSITIVE_WORDS = load_words("positive_words.txt")
NEGATIVE_WORDS = load_words("negative_words.txt")

df_reviews = pd.read_csv("Amazon Cell Phone Reviews dataset/reviews.csv")
df_items = pd.read_csv("Amazon Cell Phone Reviews dataset/items.csv")

df = (
   df_reviews.merge(df_items[["asin", "brand"]], on="asin", how="left")
   .dropna(subset=["body"])
   .reset_index(drop=True)
)

df["true_label"] = df["rating"].apply(rating_to_label)
df["tokens"] = df["body"].apply(preprocess)
df["score"] = df["tokens"].apply(lambda t: sentiment_score(t, POSITIVE_WORDS, NEGATIVE_WORDS))
df["predicted"] = df["score"].apply(classify)

eval_df = df[(df["predicted"] != "Neutral") & (df["true_label"] != "Neutral")]
accuracy = (eval_df["predicted"] == eval_df["true_label"]).mean() * 100 if not eval_df.empty else 0.0

token_freq = Counter(t for tokens in df["tokens"] for t in tokens)
top_pos = sorted(((w, token_freq[w]) for w in POSITIVE_WORDS if token_freq[w] > 0), key=lambda x: -x[1])[:5]
top_neg = sorted(((w, token_freq[w]) for w in NEGATIVE_WORDS if token_freq[w] > 0), key=lambda x: -x[1])[:5]

brand_sentiment = (
   df.dropna(subset=["brand"])
   .groupby("brand")["score"]
   .agg(avg_score="mean", review_count="count")
   .query("review_count >= 5")
   .sort_values("avg_score", ascending=False)
)

print(f"Accuracy (Pos/Neg only): {accuracy:.2f}%")
print("Top positive words:", top_pos)
print("Top negative words:", top_neg)
print("Top 5 brands by sentiment:\n", brand_sentiment.head(5).to_string())
print("Bottom 5 brands by sentiment:\n", brand_sentiment.tail(5).to_string())