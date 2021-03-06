# Generated by Django 3.0.8 on 2021-10-26 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estate',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.City'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='estate_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.Estate'),
        ),
    ]
