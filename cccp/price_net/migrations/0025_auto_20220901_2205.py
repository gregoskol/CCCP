# Generated by Django 2.2.16 on 2022-09-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0024_auto_20220901_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcprice',
            name='crossing_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='количество, шт'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='crossing_price_one',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена за ед.'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='crossing_price_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Итого, руб'),
        ),
    ]
