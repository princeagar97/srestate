from django.db import migrations,models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20210923_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=128)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255)),
                ('client_address', models.CharField(max_length=255)),
                ('contact_person', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('mobile', models.CharField(blank=True, max_length=64, null=True)),
                ('mail', models.CharField(blank=True, max_length=64, null=True)),
                ('client_details', models.TextField(blank=True, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_time', models.TextField()),
                ('contact_details', models.TextField()),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_name', models.CharField(max_length=255)),
                ('floor_space', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('number_of_balconies', models.IntegerField(blank=True, null=True)),
                ('balconies_space', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('number_of_bedrooms', models.IntegerField(blank=True, null=True)),
                ('number_of_bathrooms', models.IntegerField(blank=True, null=True)),
                ('number_of_garages', models.IntegerField(blank=True, null=True)),
                ('number_of_parking_spaces', models.IntegerField(blank=True, null=True)),
                ('pets_allowed', models.IntegerField(blank=True, null=True)),
                ('estate_description', models.TextField()),
            ],
            options={
                'managed': True,
            },
        )]