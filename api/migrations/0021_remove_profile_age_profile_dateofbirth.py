# Generated by Django 5.1.6 on 2025-02-26 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_profile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Age',
        ),
        migrations.AddField(
            model_name='profile',
            name='DateOfbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
