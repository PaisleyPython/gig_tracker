# Generated by Django 5.0.2 on 2024-03-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_alter_confirmedgigs_additional_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmedgigs',
            name='additional_info',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]