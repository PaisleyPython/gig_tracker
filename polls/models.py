import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from users.models import Profile
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
import django.db.models.deletion


def profileUpdated(sender, instance, created, **kwargs):
    print('Profile Saved')


post_save.connect(profileUpdated, sender=Profile)


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=True)
    # tags = models.ManyToManyField('NameTag', null=True, blank=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(
        max_length=200, null=True, blank=True)
    votes = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    poll = models.ForeignKey(
        Question, on_delete=django.db.models.deletion.SET_NULL, related_name="user_votes", null=True, blank=True)
    choice = models.ForeignKey(
        Choice, django.db.models.deletion.SET_NULL, related_name="user_votes", null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=django.db.models.deletion.SET_NULL, related_name="user_votes", null=True, blank=True)

    class Meta:
        unique_together = ('poll', 'user',)

    # def __str__(self):
    #     return self.choice


class ConfirmedGigs(models.Model):
    request = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100, null=True, blank=True)
    fee = models.CharField(max_length=10, null=True, blank=True)
    set_type = models.CharField(max_length=50, null=True, blank=True)
    additional_info = models.TextField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(to='NameTag', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    confirmed = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.venue


class NameTag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
