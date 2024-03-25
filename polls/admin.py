from typing import Any
from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Choice, Question, ConfirmedGigs, NameTag, Vote


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 2
#     max_num = 2


class ChoiceInLineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        kwargs['initial'] = [
            {'choice_text': 'Yay'}, {'choice_text': 'Nay'}
        ]
        super(ChoiceInLineFormset, self).__init__(*args, **kwargs)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 2
    formset = ChoiceInLineFormset

    def save_model(self, request, obj, form, change):
        form.cleaned_data['choice_text'] = Choice.objects.filter(
            pk__in=dict(request.POST).get('choice_text'))
        super(ChoiceInline, self).save_model(request, obj, form, change)


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]})
    ]

    inlines = [ChoiceInline]
    list_display = ["question_text"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(ConfirmedGigs)
admin.site.register(NameTag)
admin.site.register(Vote)
