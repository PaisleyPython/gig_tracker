# Generated by Django 5.0.2 on 2024-03-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0048_remove_nametag_request_nametag_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametag',
            name='request',
        ),
        migrations.AddField(
            model_name='confirmedgigs',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='polls.nametag'),
        ),
    ]