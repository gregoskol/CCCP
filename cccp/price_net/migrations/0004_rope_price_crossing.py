# Generated by Django 2.2.16 on 2022-08-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0003_rope_price_oogen'),
    ]

    operations = [
        migrations.AddField(
            model_name='rope',
            name='price_crossing',
            field=models.FloatField(blank=True, null=True, verbose_name='Скрещивание'),
        ),
    ]
