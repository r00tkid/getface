# Generated by Django 2.1.3 on 2019-01-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=30, verbose_name='Телефон'),
        ),
    ]
