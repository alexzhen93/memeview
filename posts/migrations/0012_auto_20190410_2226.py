# Generated by Django 2.1.7 on 2019-04-11 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20190410_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.ImageField(default=None, upload_to='memes'),
        ),
    ]