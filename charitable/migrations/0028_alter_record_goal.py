# Generated by Django 3.2.13 on 2022-05-03 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0027_auto_20220503_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record', to='charitable.goal'),
        ),
    ]
