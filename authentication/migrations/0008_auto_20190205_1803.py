# Generated by Django 2.1.5 on 2019-02-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20190205_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation',
            field=models.CharField(default='c828dbc4719e97be18ec6bb76ca61f95', editable=False, max_length=255, null=True, verbose_name='Код активации/восстановления пароля'),
        ),
    ]