# Generated by Django 3.2.7 on 2021-09-22 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_book_avilable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='avilable',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='YES', max_length=20),
        ),
    ]
