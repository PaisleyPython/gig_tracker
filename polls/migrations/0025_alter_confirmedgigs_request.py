# Generated by Django 5.0.2 on 2024-03-11 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_alter_confirmedgigs_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmedgigs',
            name='request',
            field=models.CharField(max_length=100),
        ),
    ]
