# Generated by Django 4.2 on 2023-05-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='summary',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='Default description', max_length=255),
        ),
    ]
