# Generated by Django 2.2.16 on 2022-09-02 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0026_auto_20220902_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calcprice',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Расчет №'),
        ),
    ]
