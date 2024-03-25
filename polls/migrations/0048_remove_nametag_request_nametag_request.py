# Generated by Django 5.0.2 on 2024-03-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0047_nametag_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametag',
            name='request',
        ),
        migrations.AddField(
            model_name='nametag',
            name='request',
            field=models.ManyToManyField(blank=True, null=True, to='polls.question'),
        ),
    ]
