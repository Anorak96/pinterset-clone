# Generated by Django 4.2.7 on 2024-03-14 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='pin_tag',
            field=models.ManyToManyField(related_name='post_tag', to='post.tag'),
        ),
    ]