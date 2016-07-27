from django.contrib import admin
from social_twitter.models import Tweet

# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_at','sentiment','score' )

admin.site.register(Tweet, TweetAdmin)
