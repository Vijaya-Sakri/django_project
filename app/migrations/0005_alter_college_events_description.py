# Generated by Django 4.2.1 on 2023-06-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_college_events_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_events',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
