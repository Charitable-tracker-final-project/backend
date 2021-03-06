# Generated by Django 3.2.13 on 2022-05-01 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charitable', '0021_auto_20220430_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='donationgoal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationgoalorg', to='charitable.donationgoal'),
        ),
        migrations.AddField(
            model_name='organization',
            name='volunteergoal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteergoalorg', to='charitable.volunteergoal'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(blank=True, choices=[('Animals', 'Animals'), ('Arts Culture Humanities', 'Arts Culture Humanities'), ('Asian Rights', 'Asian Rights'), ('Black Rights', 'Black Rights'), ('Community Development', 'Community Development'), ('Education', 'Education'), ('Environmental', 'Environmental'), ('Health', 'Health'), ('Human and Civil Rights', 'Human and Civil Rights'), ('Human Services', 'Human Services'), ('International', 'International'), ('Latino Rights', 'Latino Rights'), ('Research and Public Policy', 'Research and Public Policy'), ('Religion', 'Religion'), ("Women's Rights", "Women's Rights")], max_length=200)),
                ('donationgoal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='donationgoalcause', to='charitable.donationgoal')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cuser', to=settings.AUTH_USER_MODEL)),
                ('volunteergoal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='volunteergoalcause', to='charitable.volunteergoal')),
            ],
        ),
        migrations.AlterField(
            model_name='donationrecord',
            name='cause',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='causedonationrecord', to='charitable.cause'),
        ),
        migrations.AlterField(
            model_name='volunteerrecord',
            name='cause',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='causevolunteerrecord', to='charitable.cause'),
        ),
    ]
