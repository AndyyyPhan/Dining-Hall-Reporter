# Generated by Django 4.2.10 on 2024-04-09 18:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0005_remove_report_submission_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='submission_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
