# Generated by Django 5.0.2 on 2024-03-13 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_alter_confirmedgigs_request_vote'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
    ]
