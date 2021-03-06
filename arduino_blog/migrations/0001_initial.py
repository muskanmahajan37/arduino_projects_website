# Generated by Django 2.1 on 2020-02-20 07:10

import arduino_blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, choices=[('Mr', 'Mr.'), ('Miss', 'Ms.'), ('Professor', 'Prof.'), ('Doctor', 'Dr.')], max_length=32)),
                ('institute', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
                ('position', models.CharField(choices=[('student', 'Student'), ('faculty', 'Faculty')], max_length=32)),
                ('how_did_you_hear_about_us', models.CharField(blank=True, choices=[('Poster', 'Poster'), ('FOSSEE website', 'FOSSEE website'), ('Google', 'Google'), ('Social Media', 'Social Media'), ('NMEICT Blended Workshop', 'NMEICT Blended Workshop'), ('From other College', 'From other College')], max_length=255)),
                ('state', models.CharField(blank=True, choices=[('IN-AP', 'Andhra Pradesh'), ('IN-AR', 'Arunachal Pradesh'), ('IN-AS', 'Assam'), ('IN-BR', 'Bihar'), ('IN-CT', 'Chhattisgarh'), ('IN-GA', 'Goa'), ('IN-GJ', 'Gujarat'), ('IN-HR', 'Haryana'), ('IN-HP', 'Himachal Pradesh'), ('IN-JK', 'Jammu and Kashmir'), ('IN-JH', 'Jharkhand'), ('IN-KA', 'Karnataka'), ('IN-KL', 'Kerala'), ('IN-MP', 'Madhya Pradesh'), ('IN-MH', 'Maharashtra'), ('IN-MN', 'Manipur'), ('IN-ML', 'Meghalaya'), ('IN-MZ', 'Mizoram'), ('IN-NL', 'Nagaland'), ('IN-OR', 'Odisha'), ('IN-PB', 'Punjab'), ('IN-RJ', 'Rajasthan'), ('IN-SK', 'Sikkim'), ('IN-TN', 'Tamil Nadu'), ('IN-TG', 'Telangana'), ('IN-TR', 'Tripura'), ('IN-UT', 'Uttarakhand'), ('IN-UP', 'Uttar Pradesh'), ('IN-WB', 'West Bengal'), ('IN-AN', 'Andaman and Nicobar Islands'), ('IN-CH', 'Chandigarh'), ('IN-DN', 'Dadra and Nagar Haveli'), ('IN-DD', 'Daman and Diu'), ('IN-DL', 'Delhi'), ('IN-LD', 'Lakshadweep'), ('IN-PY', 'Puducherry')], max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(blank=True, max_length=6)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('activation_key', models.CharField(blank=True, max_length=255, null=True)),
                ('key_expiry_time', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name_of_author', models.CharField(default='None', max_length=200)),
                ('about_the_author', models.TextField(max_length=500)),
                ('email', models.CharField(max_length=128)),
                ('title_of_the_project', models.CharField(max_length=250)),
                ('abstract', models.TextField(max_length=700)),
                ('attachment', models.FileField(upload_to=arduino_blog.models.get_document_dir)),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('terms_and_conditions', models.BooleanField(default='True')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
