from django.shortcuts import render, render_to_response, redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf import settings

from allauth.socialaccount.models import SocialAccount, SocialToken
import tweepy
import requests , json

from .models import Tweet

# Create your views here.

consumer_key = getattr(settings, "TW_CONSUMER_KEY")
consumer_secret = getattr(settings, "TW_CONSUMER_SECRET")

def get_status_of_text(request,text, tweet):
    headers = {'content-type': 'application/json'}
    url = 'http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment'

    data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
    params = {'apikey': '67a570b1d8c91f9be817c8d4e82a521b9a6aeb71', 'text': text, 'outputMode': 'json'}
    
    try:
        res = requests.get(url, params=params)

        json_data = json.loads(res.text)
        
        sentiment = json_data['docSentiment']['type']

        score = json_data['docSentiment']['score']

        tw = Tweet(user=request.user, tweet_id=tweet.id,
                   text=text, created_at=tweet.created_at, sentiment=sentiment,
                   score=score
                   )
        tw.save()

    except:
        tw = Tweet(user=request.user, tweet_id=tweet.id,
                   text=text, created_at=tweet.created_at
                   )
        tw.save()



@login_required
@require_http_methods(['GET'])
def social_twitter_fetch(request):

    social_account = SocialAccount.objects.filter(user=request.user, provider='twitter')

    if not social_account.exists():
        return redirect('dashboard:dashboard_twitter')

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

    for tweet in user_tweets:
        if hasattr(tweet, 'retweeted_status'):
            tw_text = tweet.retweeted_status.text
        else:
            tw_text = tweet.text

        get_status_of_text(request, tw_text, tweet)


    return redirect('dashboard:dashboard_twitter')

    