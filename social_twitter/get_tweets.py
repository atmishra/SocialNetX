import tweepy
import requests , json

def fetch_tweets(social_account):
    social_token = SocialToken.objects.filter(account=social_account)[0]

        access_token = social_token.token
        access_token_secret = social_token.token_secret

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        try:
            last_tweet_fetch = Tweet.objects.filter(user=request.user).order_by('-created_at')[0]
            last_tweet_id = last_tweet_fetch.tweet_id

            user_tweets = api.user_timeline(since_id=last_tweet_id, count=100)

        except:
            user_tweets = api.user_timeline(count=100)

        return user_tweetsfrom allauth.socialaccount.models import SocialAccount, SocialToken
