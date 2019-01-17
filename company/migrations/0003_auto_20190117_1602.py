# Generated by Django 2.1.3 on 2019-01-17 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_auto_20190117_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='company.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Платильщик'),
        ),
    ]
