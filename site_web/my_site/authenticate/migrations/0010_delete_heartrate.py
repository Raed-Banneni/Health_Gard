# Generated by Django 4.2 on 2023-04-28 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0009_famille_email_pour_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HeartRate',
        ),
    ]