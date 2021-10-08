# Generated by Django 3.2.7 on 2021-09-16 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_borrowing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_borrow', models.DateField()),
                ('en_borrow', models.DateField()),
                ('return_borrow', models.DateField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='books',
            field=models.ManyToManyField(through='user.Borrowing', to='user.Book'),
        ),
    ]
