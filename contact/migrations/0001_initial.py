# Generated by Django 3.2 on 2021-04-17 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Row Name')),
                ('email', models.EmailField(max_length=100, verbose_name='E-Mail Me')),
                ('phone', models.CharField(max_length=255, verbose_name='Location')),
            ],
        ),
    ]