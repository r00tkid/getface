# Generated by Django 2.1.4 on 2019-01-21 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название компании')),
                ('description', models.TextField(blank=True, max_length=4000, null=True, verbose_name='Описание компании')),
                ('address', models.CharField(blank=True, max_length=512, null=True, verbose_name='Адрес компании')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Телефон')),
                ('email', models.CharField(max_length=255, verbose_name='Почтовый ящик')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('info', models.TextField(default='{}', verbose_name='Информация о платеже')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.Company', verbose_name='Компания')),
            ],
            options={
                'verbose_name': 'Оплата',
                'verbose_name_plural': 'Оплаты',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('per_month', models.FloatField(verbose_name='Цена за месяц (руб)')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Архивный')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Телефон')),
                ('is_manager', models.BooleanField(default=False, verbose_name='Менеджер')),
                ('is_fired', models.BooleanField(default=False, verbose_name='Уволен')),
                ('auth_key', models.UUIDField(default=uuid.uuid4, editable=False, null=True, unique=True, verbose_name='Уникальный авторизационный ключ')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='E-mail')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Компания')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Физический пользователь')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Rate'),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Платильщик'),
        ),
        migrations.AlterUniqueTogether(
            name='worker',
            unique_together={('user', 'company')},
        ),
    ]
