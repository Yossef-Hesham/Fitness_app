# Generated by Django 5.1.6 on 2025-02-25 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_profile_height_alter_profile_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='picture',
        ),
    ]
