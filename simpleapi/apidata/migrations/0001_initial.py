# Generated by Django 4.1.3 on 2023-03-28 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('tskills', models.CharField(max_length=6000)),
                ('sskills', models.CharField(max_length=6000)),
            ],
        ),
    ]
