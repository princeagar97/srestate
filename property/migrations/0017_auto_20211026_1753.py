# Generated by Django 3.0.8 on 2021-10-26 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20211026_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='estate_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='property.Estate'),
        ),
    ]
