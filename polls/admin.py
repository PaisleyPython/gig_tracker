from django.contrib import admin

from .models import Choice, Question, ConfirmedGigs, NameTag


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


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
