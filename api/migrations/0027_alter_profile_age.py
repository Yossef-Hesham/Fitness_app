# Generated by Django 5.1.6 on 2025-02-26 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Age',
            field=models.FloatField(max_length=4, null=True),
        ),
    ]
