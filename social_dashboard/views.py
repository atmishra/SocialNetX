from django.shortcuts import render, render_to_response

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from allauth.socialaccount.models import SocialAccount, SocialToken

from social_twitter.models import Tweet

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

    return render(request, 'social_dashboard_twitter.html', {'tweets': tweets})
