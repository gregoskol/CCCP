# Generated by Django 2.2.16 on 2022-09-02 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_net', '0028_auto_20220902_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='calcprice',
            name='braid_oogen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='br_oo', to='price_net.Rope', verbose_name='Заплетка огона'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='braid_oogen_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='количество, шт'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='braid_oogen_price_one',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена за ед.'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='braid_oogen_price_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Итого, руб'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='splice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='splice', to='price_net.Rope', verbose_name='Сплесень'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='splice_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='количество, шт'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='splice_price_one',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена за ед.'),
        ),
        migrations.AddField(
            model_name='calcprice',
            name='splice_price_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Итого, руб'),
        ),
    ]
