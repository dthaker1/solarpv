# Generated by Django 3.1.2 on 2021-11-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20211104_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancedata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]