# Generated by Django 3.2.8 on 2021-11-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20211116_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cellphone',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='officephone',
            field=models.IntegerField(blank=True),
        ),
    ]