# Generated by Django 2.2.16 on 2022-09-02 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0027_auto_20220902_0828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calcprice',
            options={'ordering': ['-number'], 'verbose_name': 'Расчет', 'verbose_name_plural': 'Расчеты'},
        ),
    ]