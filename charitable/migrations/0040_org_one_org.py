# Generated by Django 3.2.13 on 2022-05-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0039_cause_one_cause'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='org',
            constraint=models.UniqueConstraint(fields=('organization',), name='one_org'),
        ),
    ]
