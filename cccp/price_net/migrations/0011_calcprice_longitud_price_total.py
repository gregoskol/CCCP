# Generated by Django 2.2.16 on 2022-09-01 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0010_calcprice_longitud_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcprice',
            name='longitud_price_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Итого, руб'),
        ),
    ]
