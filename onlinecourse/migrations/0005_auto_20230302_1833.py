# Generated by Django 3.1.3 on 2023-03-02 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_remove_question_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='text',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]