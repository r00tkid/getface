# Generated by Django 2.1.7 on 2019-04-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_image_original_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='original_name',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Описание'),
        ),
    ]