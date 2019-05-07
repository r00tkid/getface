# Generated by Django 2.1.7 on 2019-04-11 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='image',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='Ключ'),
        ),
    ]
