# Generated by Django 5.0.2 on 2024-03-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0035_remove_confirmedgigs_tags_confirmedgigs_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='voter_tag',
            field=models.ManyToManyField(blank=True, to='polls.nametag'),
        ),
    ]
