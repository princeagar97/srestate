# Generated by Django 3.0.8 on 2021-09-24 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_remove_apartment_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.City'),
        ),
    ]
