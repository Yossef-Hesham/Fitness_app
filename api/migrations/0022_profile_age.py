# Generated by Django 5.1.6 on 2025-02-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_profile_age_profile_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Age',
            field=models.FloatField(default=100, max_length=4),
        ),
    ]
