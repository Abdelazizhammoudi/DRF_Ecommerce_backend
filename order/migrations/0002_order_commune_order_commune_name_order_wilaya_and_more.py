# Generated by Django 4.2.2 on 2025-04-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='commune',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='commune_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='wilaya',
            field=models.CharField(default='01', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='wilaya_name',
            field=models.CharField(default='adrar', max_length=100),
        ),
    ]
