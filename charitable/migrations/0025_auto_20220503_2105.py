# Generated by Django 3.2.13 on 2022-05-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0024_auto_20220503_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='donationgoal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='goal',
            name='volunteergoal',
            field=models.IntegerField(null=True),
        ),
    ]