# Generated by Django 3.0.10 on 2021-03-07 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mapbox_location_field.models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('GOV', 'GOVERNMENT'), ('PRIV', 'PRIVATE INSTITUTION')], max_length=150)),
                ('status', models.CharField(choices=[('NOT OPERATIONAL', 'NOT OPERATIONAL'), ('OPERATION', 'OPERATIONAL')], max_length=50)),
                ('logo', models.ImageField(null=True, upload_to='media/')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={'center': [36.8219, -1.2921], 'marker_color': 'blue', 'zoom': 8})),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(null=True)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ambulance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('plate_number', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('BASIC', 'Basic Ambulance'), ('ADVANCE', 'Advance Ambulance'), ('MORTUARY', 'Mortuary Ambulance'), ('Neonatal', 'Neonatal Ambulance'), ('Patient-Transport', 'Patient Transport Vehicle'), ('Air', 'Air Ambulance')], max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('services', models.TextField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('ENGAGED', 'ENGAGED')], default='AVAILABLE', max_length=50)),
                ('capacity', models.IntegerField()),
                ('request_contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.Institution')),
            ],
        ),
    ]
