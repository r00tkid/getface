# Generated by Django 2.1.3 on 2019-01-17 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20190117_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.Company', verbose_name='Компания'),
        ),
    ]