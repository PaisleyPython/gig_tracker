# Generated by Django 5.0.2 on 2024-03-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_rename_choice_nay_choice_choice_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
