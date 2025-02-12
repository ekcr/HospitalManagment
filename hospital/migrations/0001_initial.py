# Generated by Django 5.0.7 on 2024-07-22 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=35)),
                ('department', models.CharField(db_column='Departmant', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=35)),
                ('age', models.IntegerField(blank=True, db_column='Age')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('doctor', models.ForeignKey(db_column='Doctor', on_delete=django.db.models.deletion.CASCADE, to='hospital.doctors')),
                ('patient', models.ForeignKey(db_column='Patient', on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
