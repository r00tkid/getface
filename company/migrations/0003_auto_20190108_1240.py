# Generated by Django 2.1.3 on 2019-01-08 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0002_auto_20190105_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Физический пользователь'
            ),
        ),
    ]