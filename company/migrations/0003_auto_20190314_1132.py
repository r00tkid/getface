# Generated by Django 2.1.5 on 2019-03-14 11:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0002_auto_20190314_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetails',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 11, 32, 30, 340830, tzinfo=utc), verbose_name='Дата начала действия тарифа'),
        ),
    ]