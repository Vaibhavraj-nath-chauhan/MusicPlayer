# Generated by Django 3.1.4 on 2021-01-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(default='Not Defined', max_length=30),
        ),
    ]
