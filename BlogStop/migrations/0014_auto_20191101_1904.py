# Generated by Django 2.2.5 on 2019-11-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogStop', '0013_post_post_image_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image_url',
            field=models.URLField(max_length=400),
        ),
    ]