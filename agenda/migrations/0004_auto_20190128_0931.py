# Generated by Django 2.1.4 on 2019-01-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20190124_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='active',
            field=models.SmallIntegerField(default=0, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='fatigue',
            field=models.SmallIntegerField(default=0, verbose_name='Усталость'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='mood',
            field=models.SmallIntegerField(default=0, verbose_name='Настроение'),
        ),
    ]