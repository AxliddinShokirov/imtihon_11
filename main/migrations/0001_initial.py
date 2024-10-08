# Generated by Django 5.1 on 2024-08-09 18:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dsfv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Xodimlar_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('isinstance', models.BooleanField(default=False)),
                ('xodimlar_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='main.xodimlar_name')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('xodimlar_name', 'date'), name='unique_attendance_per_day')],
            },
        ),
    ]
