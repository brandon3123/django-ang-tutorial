# Generated by Django 3.0.5 on 2020-04-19 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]