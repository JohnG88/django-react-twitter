from django.conf import settings
from django.db import models

from django.db.models.signals import post_save

# Create your models here.

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

# method is user_is_saved(so you have to use the function name)
# post_save signals are sender instance created
# instance is class being saved, so user = instance
def user_did_save(sender, instance, created, *args, **kwargs):
    # if have a bunch of users created then use line below
    # Profile.objects.get_or_create(user=instance)
    if created:
        # can create a new profile
        Profile.objects.get_or_create(user=instance)
# to use the function with signal
# adding sender is telling signal what object are you tracking after model is saved(so in this case it will be User model)
# so after user model is saved it will trigger user_did_save function
post_save.connect(user_did_save, sender=User)

# can create custom users
    # after the user logs in -> verify profile