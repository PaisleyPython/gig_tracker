from django.forms import ModelForm
from django import forms
from .models import ConfirmedGigs, Question


class ConfirmedGigsForm(ModelForm):
    class Meta:
        model = ConfirmedGigs
        fields = ['request', 'venue', 'fee',
                  'set_type', 'additional_info']


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.TextInput(attrs={'placeholder': 'Date: xx/xx/xxxx'}),
        }
