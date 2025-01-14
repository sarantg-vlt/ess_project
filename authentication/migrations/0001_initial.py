# Generated by Django 5.0.6 on 2024-12-24 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('reset_token', models.CharField(blank=True, max_length=255, null=True)),
                ('token_expiration', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(max_length=50, unique=True)),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.CharField(max_length=50, unique=True)),
                ('location_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ManagingDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('reset_token', models.CharField(blank=True, max_length=255, null=True)),
                ('token_expiration', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_number', models.CharField(max_length=50, unique=True)),
                ('shift_start_time', models.TimeField()),
                ('shift_end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.CharField(max_length=100, unique=True)),
                ('manager_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('manager_image', models.ImageField(upload_to='manager_images/')),
                ('dob', models.DateField()),
                ('hired_date', models.DateField()),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(default='manager', max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('linkedin_profile_link', models.URLField(blank=True, null=True)),
                ('reset_token', models.CharField(blank=True, max_length=64, null=True)),
                ('token_expiration', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.shift')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=50, unique=True)),
                ('employee_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('employee_image', models.ImageField(blank=True, null=True, upload_to='employee_images/')),
                ('dob', models.DateField()),
                ('hired_date', models.DateField()),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('role', models.CharField(default='employee', max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('linkedin_profile_link', models.URLField(blank=True, null=True)),
                ('reset_token', models.CharField(blank=True, max_length=64, null=True)),
                ('token_expiration', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.shift')),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_id', models.CharField(max_length=100, unique=True)),
                ('supervisor_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(max_length=10)),
                ('supervisor_image', models.ImageField(upload_to='supervisor_images/')),
                ('dob', models.DateField()),
                ('hired_date', models.DateField()),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(default='supervisor', max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=10, null=True)),
                ('linkedin_profile_link', models.URLField(blank=True, null=True)),
                ('reset_token', models.CharField(blank=True, max_length=64, null=True)),
                ('token_expiration', models.DateTimeField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.department')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.shift')),
            ],
        ),
    ]
