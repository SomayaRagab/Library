# Generated by Django 3.2.7 on 2021-09-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20210922_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='isAvilabled',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=20),
        ),
    ]
