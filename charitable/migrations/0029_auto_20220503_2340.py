# Generated by Django 3.2.13 on 2022-05-03 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0028_alter_record_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='dgoaltitle',
            new_name='goaltitle',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='vgoaltitle',
        ),
    ]
