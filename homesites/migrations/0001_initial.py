# Generated by Django 3.2 on 2023-11-02 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
        ('plans', '0001_initial'),
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homesite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_number', models.CharField(blank=True, max_length=50, null=True)),
                ('listing_picture', models.ImageField(upload_to='listings/')),
                ('rendering', models.ImageField(upload_to='renderings/')),
                ('aerial_shot', models.ImageField(upload_to='aerial_shots/')),
                ('status', models.CharField(choices=[('presale', 'Available for Presale'), ('construction', 'Under Construction'), ('ready', 'Move-in Ready')], max_length=12)),
                ('sale_status', models.CharField(choices=[('available', 'Available'), ('contract', 'Under Contract'), ('sold', 'Sold')], max_length=10)),
                ('hidden', models.BooleanField(default=True)),
                ('lot_size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addresses.address')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.community')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.plan')),
            ],
        ),
    ]
