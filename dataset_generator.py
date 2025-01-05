from datetime import timedelta
try:
    import pandas as pd
except ImportError:
    print("Please install pandas using `pip install pandas`")
    exit(1)
import random


post_types = ["carousel", "reels", "static images"]
start_date = pd.to_datetime("2021-01-01")
data_with_caption = []

for i in range(1, 1001):
    post_type = random.choice(post_types)
    likes = random.randint(500, 10000)  # Likes ranging from 500 to 10000
    shares = random.randint(50, 1000)  # Shares ranging from 50 to 1000
    comments = random.randint(20, 500)  # Comments ranging from 20 to 500
    date_posted = (start_date + timedelta(days=i % 365)).strftime("%Y-%m-%d")
    data_with_caption.append([post_type, likes, shares, comments, date_posted])

df_with_caption = pd.DataFrame(
    data_with_caption,
    columns=["post_type", "likes", "shares", "comments", "date_posted"],
)
df_with_caption.to_csv("social_media_data.csv", index=False)
