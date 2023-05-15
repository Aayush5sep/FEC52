# Generated by Django 4.2 on 2023-05-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='helperid',
            field=models.UUIDField(default='exit'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clothes',
            name='helperid',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='miscellaneous',
            name='helperid',
            field=models.UUIDField(),
        ),
    ]
