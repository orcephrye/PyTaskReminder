# Generated by Django 4.2.5 on 2023-09-08 05:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tasks",
            name="time_end",
        ),
        migrations.AddField(
            model_name="tasks",
            name="time_from",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]