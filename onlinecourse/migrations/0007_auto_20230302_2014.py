# Generated by Django 3.1.3 on 2023-03-02 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0006_auto_20230302_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
    ]
