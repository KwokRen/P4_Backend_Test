# Generated by Django 3.1.1 on 2020-09-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
