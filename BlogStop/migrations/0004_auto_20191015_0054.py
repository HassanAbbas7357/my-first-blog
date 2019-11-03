# Generated by Django 2.2.5 on 2019-10-14 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogStop', '0003_auto_20191015_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Categories'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='BlogStop.Category'),
        ),
    ]
