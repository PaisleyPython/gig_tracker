from typing import Any
from django.contrib import admin


from .models import Choice, Question, ConfirmedGigs, NameTag, Vote


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 2


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
