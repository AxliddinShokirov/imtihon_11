# Generated by Django 5.1 on 2024-08-09 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jamoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaqt', models.DateField()),
                ('jamoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='davomat', to='main.jamoa')),
            ],
        ),
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('jamoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='xodiumlar', to='main.jamoa')),
            ],
        ),
        migrations.CreateModel(
            name='Damovat_olish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attendes', models.BooleanField(default=False)),
                ('davomat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damovat_olish', to='main.davomat')),
                ('xodim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='damovat_olish', to='main.xodimlar')),
            ],
            options={
                'unique_together': {('davomat', 'xodim')},
            },
        ),
    ]
