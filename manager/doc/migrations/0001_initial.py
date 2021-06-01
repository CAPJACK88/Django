# Generated by Django 3.2.3 on 2021-06-01 10:12

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, max_length=1000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(blank=True, max_length=1000, verbose_name='Описание')),
                ('document', models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Документ')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('publications', models.BooleanField(default=False, verbose_name='Опубликовоно')),
                ('category', models.ManyToManyField(to='doc.Category', verbose_name='Категория')),
                ('username', models.ManyToManyField(blank=True, to='user.User', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['date_creation'],
            },
        ),
    ]
