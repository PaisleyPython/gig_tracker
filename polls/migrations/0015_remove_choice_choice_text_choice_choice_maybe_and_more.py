# Generated by Django 5.0.2 on 2024-03-10 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_choice_choice_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_maybe',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_nay',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_yay',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
