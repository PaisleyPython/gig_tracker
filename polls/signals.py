from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Choice
import os
from twilio.rest import Client

# TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
# MY_PHONE_NUMBER = os.getenv('MY_PHONE_NUMBER ')
# TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# # TODO Figure out why code is running twice. Likely to do with the fact that 'question_choice' has 2 fields.


# @receiver(post_save, sender=Choice)
# def createPoll(sender, instance, created, **kwargs):
#     print('Created: ', created)
#     if created:
#         print(TWILIO_AUTH_TOKEN)
#         account_sid = os.environ[TWILIO_ACCOUNT_SID]
#         auth_token = os.environ[TWILIO_AUTH_TOKEN]
#         client = Client(account_sid, auth_token)

#         message = client.messages \
#                         .create(
#                             body="A gig poll has been created.\nHead to www.discopanther.com to state your availability.\nNO REPLY ",
#                             from_=TWILIO_PHONE_NUMBER,
#                             to=MY_PHONE_NUMBER
#                         )

#         print(message.sid)

# post_save.connect(createPoll, sender=Choice)


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure


# Working with signals, i dont want the poll to be created after gig is created.
# The sequence needs to be..
# Create poll > send signal to members > then once x amount of members vote in favour > auto populate create gig form to later be updated with additional information.
