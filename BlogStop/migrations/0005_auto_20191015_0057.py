# Generated by Django 2.2.5 on 2019-10-14 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogStop', '0004_auto_20191015_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='post_image_url',
        ),
    ]
