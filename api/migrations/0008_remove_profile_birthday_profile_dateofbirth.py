# Generated by Django 5.1.6 on 2025-02-13 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_exercise_weight_alter_exercise_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Birthday',
        ),
        migrations.AddField(
            model_name='profile',
            name='DateOfbirth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
