# Generated by Django 3.0.8 on 2021-09-23 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_estatetype_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
