# Generated by Django 2.1.3 on 2019-01-17 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkerAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('start', models.DateTimeField(verbose_name='Дата начала')),
                ('end', models.DateTimeField(verbose_name='Дата окончания')),
                ('is_wanted', models.BooleanField(blank=True, default=None, null=True, verbose_name='Хочет работать')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Worker', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'График работника',
                'verbose_name_plural': 'Графики работника',
            },
        ),
        migrations.CreateModel(
            name='WorkerFaceTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date record created')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date record updated')),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('start', models.DateTimeField(verbose_name='Дата начала')),
                ('end', models.DateTimeField(verbose_name='Дата окончания')),
                ('active', models.IntegerField(default=0, verbose_name='Активность')),
                ('mood', models.IntegerField(default=0, verbose_name='Настроение')),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Worker', verbose_name='Работник')),
            ],
            options={
                'verbose_name': 'Показатель работника',
                'verbose_name_plural': 'Показатели работника',
            },
        ),
    ]