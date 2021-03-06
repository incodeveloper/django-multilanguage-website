# Generated by Django 3.2 on 2021-04-17 19:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_remove_page_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('alt', models.CharField(max_length=100, verbose_name='Alt')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Header Section',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('alt', models.CharField(max_length=100, verbose_name='Alt')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('resume', models.FileField(upload_to='', verbose_name='CV')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('icon', models.ImageField(upload_to='', verbose_name='Icon')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(verbose_name='Text')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Name')),
                ('detail', models.TextField(verbose_name='Detail')),
                ('video', models.TextField(verbose_name='Embed Code')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Video Section',
            },
        ),
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HeaderSplitText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=80, verbose_name='Text')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='header_section', to='page.headersection')),
            ],
            options={
                'verbose_name_plural': 'Split Text',
            },
        ),
    ]
