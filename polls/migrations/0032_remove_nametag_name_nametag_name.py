# Generated by Django 5.0.2 on 2024-03-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0031_remove_nametag_vote_vote_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametag',
            name='name',
        ),
        migrations.AddField(
            model_name='nametag',
            name='name',
            field=models.ManyToManyField(max_length=50, to='polls.vote'),
        ),
    ]
