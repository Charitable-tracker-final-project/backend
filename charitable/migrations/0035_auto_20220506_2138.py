# Generated by Django 3.2.13 on 2022-05-06 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0034_orgdonation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CauseDonation',
            new_name='Cause',
        ),
        migrations.RenameModel(
            old_name='OrgDonation',
            new_name='Org',
        ),
        migrations.RemoveField(
            model_name='record',
            name='cause',
        ),
        migrations.RemoveField(
            model_name='record',
            name='organization',
        ),
    ]
