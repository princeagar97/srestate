# Generated by Django 3.0.8 on 2021-10-26 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20211026_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.Client'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.Broker'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='estate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='property.Estate'),
        ),
        migrations.AlterField(
            model_name='estate',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estate',
            name='estate_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.EstateStatus'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estate',
            name='estate_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.EstateType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incharge',
            name='broker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.Broker'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incharge',
            name='estate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.Estate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photos',
            name='estate_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.Estate'),
        ),
        migrations.AlterField(
            model_name='subestatetype',
            name='estate_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='property.EstateType'),
            preserve_default=False,
        ),
    ]