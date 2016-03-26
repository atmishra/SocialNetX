from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from SocialNetX.users.models import User

# Create your models here.


@python_2_unicode_compatible
class Tweet(models.Model):

    user = models.ForeignKey(User)
    tweet_id = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.text
