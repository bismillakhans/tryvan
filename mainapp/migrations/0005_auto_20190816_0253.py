# Generated by Django 2.2.4 on 2019-08-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20190816_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='file',
        ),
        migrations.AddField(
            model_name='paper',
            name='file_up',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d', verbose_name='Document'),
        ),
    ]
