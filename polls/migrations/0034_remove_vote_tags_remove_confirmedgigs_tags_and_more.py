# Generated by Django 5.0.2 on 2024-03-17 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_remove_nametag_name_nametag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='confirmedgigs',
            name='tags',
        ),
        migrations.AddField(
            model_name='confirmedgigs',
            name='tags',
            field=models.CharField(blank=True, max_length=50, verbose_name='NameTag'),
        ),
    ]
