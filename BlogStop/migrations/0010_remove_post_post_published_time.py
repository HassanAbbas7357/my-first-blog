# Generated by Django 2.2.5 on 2019-10-30 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogStop', '0009_auto_20191031_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_published_time',
        ),
    ]