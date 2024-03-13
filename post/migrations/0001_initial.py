# Generated by Django 4.2.7 on 2024-03-13 07:41

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
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.ImageField(upload_to='pins')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile_post', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(related_name='pin_tags', to='post.tag')),
            ],
        ),
    ]
