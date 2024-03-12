from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile

# @receiver(post_save, sender=Profile)


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
    # print('Profile Saved')
    # print('Instance', instance)
    # print('CREATED', created)


def deleteUser(sender, instance, **kwargs):
    print('Deleting User..')


post_save.connect(createProfile, sender=User)


post_delete.connect(deleteUser, sender=Profile)
