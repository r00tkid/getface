# Generated by Django 2.1.5 on 2019-02-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_activation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation',
            field=models.CharField(default='591d7c4851a391887c30242907a2ec0c', editable=False, max_length=255, null=True, verbose_name='Код активации/восстановления пароля'),
        ),
    ]
