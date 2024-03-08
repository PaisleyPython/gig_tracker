# Generated by Django 5.0.2 on 2024-03-08 05:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_confirmedgigs_additional_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='members',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='confirmedgigs',
            name='gig_vote',
        ),
        migrations.AddField(
            model_name='confirmedgigs',
            name='request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.question'),
        ),
    ]
