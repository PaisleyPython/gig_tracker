# Generated by Django 5.0.2 on 2024-03-17 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0037_remove_choice_voter_tag_question_voter_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='voter_tag',
        ),
    ]