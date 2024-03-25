# Generated by Django 5.0.2 on 2024-03-19 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0043_remove_confirmedgigs_tags_choice_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='tags',
        ),
        migrations.AddField(
            model_name='choice',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.nametag'),
        ),
    ]
