# Generated by Django 2.2.16 on 2022-09-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0007_auto_20220901_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcprice',
            name='across_lenght',
            field=models.FloatField(blank=True, null=True, verbose_name='Длина, м'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='liktros_lenght',
            field=models.FloatField(blank=True, null=True, verbose_name='Длина, м'),
        ),
    ]
