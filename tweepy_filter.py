import tweepy as tw
import pandas as pd

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
access_token = "114010579-UscavtyluJ4ZOjGBGPwF3Xy8i5ynDgmeiYRLQ9WL"
access_token_secret = "hnA5I14kCwovdQF1Ciyz3VWOJlPlre8jHEKoeb9OshhJe"
consumer_key = "j2BhP2Q3LFCzpPQ5o0Xx4GuY7"
consumer_secret = "vkcmHL1U71cpqdn1LBl7GY4cdJIkvFotKAyZeChIuHBoq5aQ2j"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_words = "#khaleesi"
date_since = "2018-05-01"


tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(20)
for tweet in tweets:
    print(tweet)