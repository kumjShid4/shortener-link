# Generated by Django 2.0.3 on 2018-07-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0008_url_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='status',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10),
        ),
    ]
