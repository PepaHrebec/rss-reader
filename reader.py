import feedparser

url = "https://www.example.com/rss"
feed = feedparser.parse(url)

with open('rss.txt', 'w') as f:
    f.write(f"{feed}")

print("Done!")