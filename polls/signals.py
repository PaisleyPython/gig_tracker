from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Choice


@receiver(post_save, sender=Choice)
def createPoll(sender, instance, created, **kwargs):
    print('Created: ', created)
    if created:
        pass

# post_save.connect(createPoll, sender=Choice)


# Working with signals, i dont want the poll to be created after gig is created.
# The sequence needs to be..
# Create poll > send signal to members > then once x amount of members vote in favour > auto populate create gig form to later be updated with additional information.
