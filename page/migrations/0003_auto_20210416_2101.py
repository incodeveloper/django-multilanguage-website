# Generated by Django 3.2 on 2021-04-16 21:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_page_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('alt', models.CharField(max_length=120, verbose_name='Alt Text')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Detail')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('alt', models.CharField(max_length=120, verbose_name='Alt Text')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Detail')),
                ('cv_file', models.FileField(upload_to='', verbose_name='CV')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='', verbose_name='Icon')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Detail')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Detail')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('video', models.TextField(verbose_name='Video Code')),
                ('content', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Detail')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
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
                ('text', models.CharField(max_length=120, verbose_name='Alt Text')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='header_section', to='page.headersection')),
            ],
        ),
    ]
