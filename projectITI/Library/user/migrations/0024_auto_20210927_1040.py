# Generated by Django 3.2.7 on 2021-09-27 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_remove_borrowing_isavilabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='return_borrow',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='borrowing',
            name='st_borrow',
            field=models.DateField(null=True),
        ),
    ]