import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from users.models import Profile
import uuid


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    # tags = models.ManyToManyField('NameTag', blank=True)

    def __str__(self):
        return self.choice_text


class ConfirmedGigs(models.Model):
    request = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    venue = models.CharField(max_length=100)
    fee = models.CharField(max_length=10, null=True, blank=True)
    set_type = models.CharField(max_length=50, null=True, blank=True)
    additional_info = models.TextField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('NameTag', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.venue


class NameTag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name
