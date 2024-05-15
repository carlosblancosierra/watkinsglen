# Generated by Django 3.2 on 2024-05-15 15:49

from django.db import migrations, models
import django.db.models.deletion
import image.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ImageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=image.models.upload_to)),
                ('tags', models.ManyToManyField(blank=True, to='image.ImageTag')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.gallery')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.image')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
