# Generated by Django 4.2.5 on 2023-09-21 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reason', models.CharField(max_length=500)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('status', models.CharField(default='Pending', max_length=200)),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leave_app.employee')),
            ],
            options={
                'db_table': 'leave',
            },
        ),
    ]
