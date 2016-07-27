from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from SocialNetX.users.models import User

# Create your models here.


@python_2_unicode_compatible
class Tweet(models.Model):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'
    
    SENTIMENT_CHOICES = (
        (POSITIVE, 'positive'),
        (NEGATIVE, 'negative'),
        (NEUTRAL, 'neutral'),
        
    )
    user = models.ForeignKey(User)
    tweet_id = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    sentiment = models.CharField(max_length=15,
                                 choices=SENTIMENT_CHOICES, blank=True)
    score = models.DecimalField(max_digits=4,decimal_places=2,default=0.0)

    def __str__(self):
        return self.text
