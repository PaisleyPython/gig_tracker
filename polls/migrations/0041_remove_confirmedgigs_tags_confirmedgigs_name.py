# Generated by Django 5.0.2 on 2024-03-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0040_confirmedgigs_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmedgigs',
            name='tags',
        ),
        migrations.AddField(
            model_name='confirmedgigs',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]