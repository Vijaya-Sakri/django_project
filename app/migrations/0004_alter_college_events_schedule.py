# Generated by Django 4.2.1 on 2023-06-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_college_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_events',
            name='schedule',
            field=models.DateField(max_length=100),
        ),
    ]
