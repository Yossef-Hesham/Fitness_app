# Generated by Django 5.1.6 on 2025-02-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Age',
            field=models.IntegerField(max_length=2, null=True),
        ),
    ]
