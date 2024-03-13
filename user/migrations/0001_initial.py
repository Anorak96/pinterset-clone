# Generated by Django 4.2.7 on 2024-03-12 17:35

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='username')),
                ('bio', models.TextField(blank=True, null=True)),
                ('cover_pic', models.ImageField(blank=True, default=user.models.get_default_cover_image, null=True, upload_to=user.models.get_cover_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('profile_pic', models.ImageField(blank=True, default=user.models.get_default_profile_image, null=True, upload_to=user.models.get_profile_image, validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])])),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
