# Generated by Django 5.0.2 on 2024-03-06 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
        ('users', '0002_alter_profile_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='members',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
