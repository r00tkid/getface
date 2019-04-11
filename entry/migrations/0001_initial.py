# Generated by Django 2.1.7 on 2019-04-11 10:02

import app.fields.timezone.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import entry.models.user.model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актив')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('activation', models.CharField(default=entry.models.user.model._activation_key, editable=False, max_length=255, null=True, verbose_name='Код активации/восстановления пароля')),
                ('timezone', app.fields.timezone.fields.TimeZoneField(blank=True, default='UTC', verbose_name='Локальное время пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
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
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.Feature', verbose_name='Фича')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Прогресс',
                'verbose_name_plural': 'Прогресс',
            },
        ),
    ]
