# Generated by Django 5.0.2 on 2024-03-18 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0038_remove_question_voter_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmedgigs',
            name='tags',
        ),
    ]
