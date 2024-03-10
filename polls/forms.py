from django.forms import ModelForm
from .models import ConfirmedGigs


class ConfirmedGigsForm(ModelForm):
    class Meta:
        model = ConfirmedGigs
        fields = '__all__'


# class ChoiceForm(ModelForm):
#     class Meta:
#         model = Choice
#         field = '__all__'
