# Generated by Django 2.2.16 on 2022-09-02 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0030_auto_20220902_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcprice',
            name='price_before_discount',
            field=models.FloatField(blank=True, null=True, verbose_name='Итого по расчету, руб'),
        ),
    ]
