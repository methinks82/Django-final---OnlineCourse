# Generated by Django 3.1.3 on 2023-03-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0005_auto_20230302_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.IntegerField(),
        ),
    ]
