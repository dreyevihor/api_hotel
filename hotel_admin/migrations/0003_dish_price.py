# Generated by Django 3.1.7 on 2021-05-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_admin', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.FloatField(default='0'),
        ),
    ]