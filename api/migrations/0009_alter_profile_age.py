# Generated by Django 5.1.5 on 2025-02-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_profile_birthday_profile_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Age',
            field=models.FloatField(max_length=2, null=True),
        ),
    ]
