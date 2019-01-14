# Generated by Django 2.1.3 on 2019-01-14 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_worker_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Физический пользователь'),
        ),
    ]