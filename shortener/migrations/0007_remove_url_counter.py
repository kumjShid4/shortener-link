# Generated by Django 2.0.3 on 2018-04-15 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_url_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='counter',
        ),
    ]
