# Generated by Django 3.2.13 on 2022-05-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0026_auto_20220503_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='hours',
        ),
        migrations.AddField(
            model_name='record',
            name='hoursdonated',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='amountdonated',
            field=models.IntegerField(null=True),
        ),
    ]
