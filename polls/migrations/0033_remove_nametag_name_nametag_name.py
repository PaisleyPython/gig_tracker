# Generated by Django 5.0.2 on 2024-03-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_remove_nametag_name_nametag_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nametag',
            name='name',
        ),
        migrations.AddField(
            model_name='nametag',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
