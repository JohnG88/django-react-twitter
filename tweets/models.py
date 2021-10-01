import random

from django.db import models

# Another approach of getting User model
from django.conf import settings
from django.db.models import Q


# Create your models here.

# Then get User model
User = settings.AUTH_USER_MODEL

# historical measure like
# createred a new table of TweetLike
# this through table is created just to be able to use timestamp
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Have to use 'Tweet', because tweet model is below TweetLike
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

# Both classes below allow to add to db and query db very effectively

# The Queryset is the all,filter, etc from Tweet.objects.all(), Tweet.objects.filter(), etc
class TweetQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profiles_exist = user.following.exists()
        followed_users_id = []
        if profiles_exist:
            # line below not very efficient
            # followed_users_id = #[x.user.id for x in profiles]
            # better query below, cuz just finding user id instead of whole user data
            followed_users_id = user.following.values_list('user__id', flat=True)

        # using user__id__in will allow to view all objects in a list and find all related
        # lin below says filter Tweet objects that have user id in followed user's id or user of user, .distinct() means no duplicates, order by created data
        # self replaces Model.objects
        return self.filter(
            Q(user__id__in=followed_users_id) | Q(user=user)
            
            ).distinct().order_by('-created')

# Manager is like objects from Tweet.objects.all()
class TweetManager(models.Manager):
    # pass in TweetQuerySet
    def get_queryset(self, *args, **kwargs):
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user):
        return self.get_queryset().feed(user)

# In shell to check for queries of user's username, use __(double underscore) ex.) qs = Tweet.objects.filter(user__username__iexact='John'), (username is the field name), (iexact means John and JOHN are the same)

'''
    retweeting is tweeting to itself, referencing another tweet, so have to get a foreignkey of tweet(itself)

    Ex.) comment
            - Reply
                - Sub Reply
            - Reply
            - Reply
    - Comment is main thing and each Reply is refencing the Comment
    - Also think of it as each Reply has a parent of Comment
    - Reply is parent of Sub Reply

    Another Example:
        - Tweet
            - Retweet
                - Retweet of Retweet

    But model is newest first
    - Retweet of Retweet
    - Retweet
    - Tweet
'''

class Tweet(models.Model):
    # setting null=True and on_delete=models.SET_NULL, will still have data, have history, backup in database
    # learn how to backup database 
    # first tweet won't have a parent only retweets
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)# adding 'self' references same model(in this case Tweet)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')# many users can have many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through='TweetLike' )
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()
    
    # reverse ascending order to descending order by id, created, etc...
    # makemigrations and migrate when doing anything with class
    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        # boolean, if parent is not = to None then it is a retweet, if parent is = to None then it is not a retweet
        return self.parent != None

    # def __str__(self):
        # return self.content


    '''
    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'created': self.created.strftime("%m-%d-%Y, %H:%M:%S"),
            'likes': random.randint(0, 1000),
        }
    '''
    '''
        When adding user model and then creating superuser, python gives me, "Trying to add a non-nullable field 'user', can add null=True, or in our case can add 1, since we are only user create so far, need to learn how to do this better"
    '''

'''
    In shell created:
        obj = Tweet.objects.first()
        - can use this because of many to many field
        obj.likes.all()
        - gives a queryset of []

    - To get User
        >>> from django.contrib.auth import get_user_model
        >>> User = get_user_model()
        >>> User.objects.all()
        <QuerySet [<User: John>]>

    - To add a User to obj.likes
        >>> me = User.objects.first()
        >>> me
        <User: John>
        >>> obj.likes.add(me)
        >>> obj.likes.all()
        <QuerySet [<User: John>]>

    - To remove User from obj.likes
        obj.likes.remove(me)

        obj.likes.all()
        QuerySet = []

    - Add multiple User's that liked
        >>> qs = User.objects.all()
        >>> obj.likes.set(qs)
        >>> obj.likes.all()
        <QuerySet [<User: John>]>

    - To add data to user and tweet fields in TweetLike
        >>> TweetLike.objects.create(user=me, tweet=obj)
        <TweetLike: TweetLike object (5)>
        >>> obj.likes.all()
        <QuerySet [<User: John>]>

    - To remove users
        >>> obj.likes.add(me)
        >>> obj.likes.all()
        <QuerySet [<User: John>]>
        >>> empty_users = User.objects.none()
        >>> empty_users
        <QuerySet []>
        >>> obj.likes.set(empty_users)
        >>> obj.likes.all()
        <QuerySet []>
'''

# Below trying to create many-to-many connection
'''
    from django.contrib.auth import get_user_model
    >>> User = get_user_model()
    >>> j = User.objects.first()
    >>> j
    <User: John>
    # so below is user through tweet model, and if there is no related_name in this user field under Tweet model then you have to use model name(lowercased)_set, in this case (tweet_set)
    # translation below is user through tweet model
    j.tweet_set.all() - will give you all tweets of user
'''

# Using related_name
'''
    In models from many-to-many connection add a realted_name attribute
    In this case we added related_name='tweets'
    Instead of using(from example above), j.tweet_set.all()
    we can use j.tweets.all(), and get the same outcome
'''

# getting all liked tweets
'''
    j.tweetlike_set.all()
'''

# can create above queryset into a variable with a one liner for loop
# not very efficient
'''
    my_likes = [x.tweet for x in j.tweetlike_set.all()]
    so now my_likes will do the same as j.tweetlike_set.all()
'''

# the best way
'''
    since the like field in Tweet model has a related_name='tweet-user', below is the most efficient way to queryset
    j.tweet_user.all()
'''

# efficient way to get length of queryset
'''
    j.tweet_user.count()
'''

