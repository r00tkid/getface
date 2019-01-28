# Generated by Django 2.1.4 on 2019-01-24 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('link', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Ссылка')),
                ('description', models.TextField(max_length=5000, verbose_name='Описание')),
                ('is_alive', models.BooleanField(default=True, verbose_name='Существует')),
                ('is_important', models.BooleanField(default=False, verbose_name='Важная')),
            ],
            options={
                'verbose_name': 'Фича',
                'verbose_name_plural': 'Фичи',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created'),
        ),
    ]