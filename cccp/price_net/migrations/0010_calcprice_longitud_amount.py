# Generated by Django 2.2.16 on 2022-09-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0009_calcprice_longitud_price_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcprice',
            name='longitud_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Количество, шт'),
        ),
    ]
