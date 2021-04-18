# Generated by Django 3.2 on 2021-04-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='facebook',
            field=models.URLField(max_length=255, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='about',
            name='instagram',
            field=models.URLField(max_length=255, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.URLField(max_length=255, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='about',
            name='twitter',
            field=models.URLField(max_length=255, null=True, verbose_name='Twitter'),
        ),
    ]