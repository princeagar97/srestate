# Generated by Django 3.0.8 on 2021-10-26 06:02

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20210924_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('estate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Estate')),
            ],
            options={
                'managed': True,
            },
        ),
    ]