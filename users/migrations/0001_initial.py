# Generated by Django 4.2 on 2023-05-15 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(blank=True, null=True)),
                ('contact', models.CharField(max_length=10)),
                ('alt_contact', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=8)),
                ('country', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50, verbose_name='Longitude')),
                ('latitude', models.CharField(max_length=50, verbose_name='Latitude')),
                ('verified', models.BooleanField(default=False)),
                ('closed', models.BooleanField(default=False)),
                ('orgn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=8)),
                ('country', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50, verbose_name='Longitude')),
                ('latitude', models.CharField(max_length=50, verbose_name='Latitude')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]