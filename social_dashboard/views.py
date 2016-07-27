from django.shortcuts import render, render_to_response

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from allauth.socialaccount.models import SocialAccount, SocialToken

from social_twitter.models import Tweet
from django.db.models import Count

# Create your views here.


@login_required
@require_http_methods(['GET'])
def social_dashboard(request):

    return render(request, 'social_dashboard.html')


@login_required
@require_http_methods(['GET'])
def social_dashboard_twitter(request):

    social_twitter_account = SocialAccount.objects.filter(user=request.user, provider='twitter').exists()

    if not social_twitter_account:
        return render(request, 'social_dashboard_twitter_add.html')

    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    score_list = [tweet.score for tweet in tweets]
    #print(score_list)

    count_neg, count_net, count_pos = 0,0,0
    if tweets:
        count_pos = len(tweets.filter(sentiment='positive'))
        count_neg = len(tweets.filter(sentiment='negative'))
        count_net = len(tweets.filter(sentiment='neutral'))


    return render(request, 'social_dashboard_twitter.html', {'tweets': tweets,
                                                             'positive_tweets': count_pos,
                                                             'negative_tweets': count_neg,
                                                             'neutral_tweets': count_net,
                                                             'scores':score_list
                                                              })

