# Generated by Django 5.0.2 on 2024-03-15 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_remove_choice_vote_ratio_nametag_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametag',
            name='vote',
        ),
        migrations.AddField(
            model_name='vote',
            name='tags',
            field=models.ManyToManyField(blank=True, to='polls.nametag'),
        ),
    ]
