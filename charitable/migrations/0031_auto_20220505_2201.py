# Generated by Django 3.2.13 on 2022-05-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0030_auto_20220503_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='amountdonated',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='hoursdonated',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
