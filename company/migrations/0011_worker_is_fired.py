# Generated by Django 2.1.3 on 2019-01-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20190110_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='is_fired',
            field=models.BooleanField(default=False, verbose_name='Уволен'),
        ),
    ]
