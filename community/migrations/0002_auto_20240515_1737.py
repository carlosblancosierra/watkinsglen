# Generated by Django 3.2 on 2024-05-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='image_front_landspace',
            field=models.ImageField(blank=True, null=True, upload_to='community-images/'),
        ),
        migrations.AlterField(
            model_name='community',
            name='image_front_portrait',
            field=models.ImageField(blank=True, null=True, upload_to='community-images/'),
        ),
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
