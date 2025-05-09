# Generated by Django 4.2.2 on 2025-04-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_rename_postalcode_order_postal_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
