from django.shortcuts import render, render_to_response, redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.conf import settings

from allauth.socialaccount.models import SocialAccount, SocialToken

from .models import Tweet

# Create your views here.

consumer_key = getattr(settings, "TW_CONSUMER_KEY")
consumer_secret = getattr(settings, "TW_CONSUMER_SECRET")

@login_required
@require_http_methods(['GET'])
def social_twitter_fetch(request):

    social_account = SocialAccount.objects.filter(user=request.user, provider='twitter')

    if not social_account.exists():
        return redirect('dashboard:dashboard_twitter')

    
    for tweet in user_tweets:
        if hasattr(tweet, 'retweeted_status'):
            tw_text = tweet.retweeted_status.text
        else:
            tw_text = tweet.text

        (sentiment,score) = get_status_of_text(request, tw_text, tweet)

        tw = Tweet(user=request.user, tweet_id=tweet.id,
                   text=text, created_at=tweet.created_at, sentiment=sentiment,
                   score=score
                   )
        tw.save()

    return redirect('dashboard:dashboard_twitter')

    