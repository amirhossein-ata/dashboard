# Generated by Django 2.0.7 on 2018-07-08 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zanbil', '0005_auto_20180705_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='restTimeEnd',
            field=models.FloatField(default=12),
        ),
        migrations.AddField(
            model_name='services',
            name='restTimeStart',
            field=models.FloatField(default=12),
        ),
    ]