# Generated by Django 2.2 on 2019-04-17 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('holding', '0006_companycreator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companycreator',
            old_name='employee',
            new_name='creator',
        ),
    ]
