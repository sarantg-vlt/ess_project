# Generated by Django 5.0.6 on 2024-10-04 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_document_document_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document_category',
        ),
        migrations.RemoveField(
            model_name='document',
            name='document_type',
        ),
        migrations.RemoveField(
            model_name='document',
            name='file',
        ),
        migrations.AddField(
            model_name='document',
            name='aadhar_card',
            field=models.FileField(blank=True, null=True, upload_to='documents/aadhar/'),
        ),
        migrations.AddField(
            model_name='document',
            name='bank_details',
            field=models.FileField(blank=True, null=True, upload_to='documents/bank/'),
        ),
        migrations.AddField(
            model_name='document',
            name='degree_certificate',
            field=models.FileField(blank=True, null=True, upload_to='documents/degree/'),
        ),
        migrations.AddField(
            model_name='document',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='experience_certificate',
            field=models.FileField(blank=True, null=True, upload_to='documents/experience/'),
        ),
        migrations.AddField(
            model_name='document',
            name='pan_card',
            field=models.FileField(blank=True, null=True, upload_to='documents/pan/'),
        ),
        migrations.AddField(
            model_name='document',
            name='previous_payslip',
            field=models.FileField(blank=True, null=True, upload_to='documents/payslip/'),
        ),
    ]
