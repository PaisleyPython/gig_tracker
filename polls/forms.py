from django.forms import ModelForm
from django import forms
from .models import ConfirmedGigs, Choice


class ConfirmedGigsForm(ModelForm):
    class Meta:
        model = ConfirmedGigs
        fields = ['request', 'venue', 'fee',
                  'set_type', 'additional_info']

    def __init__(self, *args, **kwargs):
        super(ConfirmedGigsForm, self).__init__(*args, **kwargs)

        self.fields['venue'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'E.g: Venue, City/Town'})
        self.fields['fee'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'E.g: £800.00'})
        self.fields['set_type'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'E.g: "2x 45min sets"'})
        self.fields['additional_info'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'E.g: Backline provided. Bring additional mic stands.'})

        # for name, field in self.fields.items():
        #     field.widget.attrs.update({'class': 'input'})


class QuestionForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['question']

        widgets = {
            'question': forms.TextInput(attrs={'placeholder': 'Date: xx/xx/xxxx'}),
        }
