# Generated by Django 4.0 on 2021-12-26 06:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_rename_description_doctor_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('available_days', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], default='Monday', max_length=3, verbose_name='Available Days')),
                ('start_time', models.TimeField(default=django.utils.timezone.now, verbose_name='Start Time')),
                ('end_time', models.TimeField(default=django.utils.timezone.now, verbose_name='End Time')),
                ('description', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='hospital.doctor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
