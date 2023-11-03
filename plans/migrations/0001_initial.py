# Generated by Django 3.2 on 2023-11-02 17:59

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
                ('floorplan', models.FileField(upload_to='floorplans/')),
                ('rendering', models.ImageField(upload_to='renderings/')),
                ('rooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('half_baths', models.PositiveIntegerField()),
            ],
        ),
    ]