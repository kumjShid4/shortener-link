# Generated by Django 2.0.3 on 2018-04-15 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener', '0004_auto_20180414_0154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClickCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shortener.URL')),
            ],
        ),
    ]
