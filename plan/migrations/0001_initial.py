# Generated by Django 4.0.10 on 2024-05-04 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('floorplan', models.FileField(blank=True, null=True, upload_to='floorplans/')),
                ('rendering', models.ImageField(blank=True, null=True, upload_to='renderings/')),
                ('sqft', models.PositiveIntegerField(blank=True, null=True)),
                ('rooms', models.PositiveIntegerField(blank=True, null=True)),
                ('bathrooms', models.PositiveIntegerField(blank=True, null=True)),
                ('half_baths', models.PositiveIntegerField(blank=True, null=True)),
                ('plan_library', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
