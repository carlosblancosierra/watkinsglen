# Generated by Django 3.2 on 2024-05-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20240515_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='community',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
