# Generated by Django 2.1.5 on 2019-02-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_auto_20190206_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation',
            field=models.CharField(default='48f04b069dda70cd89a8b5ea5baed1f3', editable=False, max_length=255, null=True, verbose_name='Код активации/восстановления пароля'),
        ),
    ]
