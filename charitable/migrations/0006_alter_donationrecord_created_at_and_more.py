# Generated by Django 4.0.4 on 2022-04-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0005_alter_donationrecord_donationreceipt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationrecord',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='volunteerrecord',
            name='created_at',
            field=models.DateField(),
        ),
    ]
