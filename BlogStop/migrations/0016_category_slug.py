# Generated by Django 2.2.5 on 2019-11-01 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogStop', '0015_auto_20191101_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='abc'),
        ),
    ]
