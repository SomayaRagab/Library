# Generated by Django 3.2.7 on 2021-09-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_borrowing_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
        migrations.AddField(
            model_name='user',
            name='confirm',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
