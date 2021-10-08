# Generated by Django 3.2.7 on 2021-09-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('author', models.CharField(max_length=20, null=True)),
                ('price', models.FloatField(null=True)),
                ('img', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('Classics', 'Classics'), ('Comic Book', 'Comic Book'), ('Learning', 'Learning')], max_length=20)),
                ('des', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('password', models.CharField(max_length=8, null=True)),
                ('role', models.CharField(choices=[('user', 'user'), ('admin', 'admin')], default='user', max_length=20)),
            ],
        ),
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
    ]