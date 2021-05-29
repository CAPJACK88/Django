# Generated by Django 3.2 on 2021-05-29 19:04

from django.db import migrations, models
import django.db.models.deletion


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
                ('title', models.CharField(max_length=500, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
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
                ('title', models.CharField(max_length=500, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='Описание')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('document', models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Документ')),
                ('publications', models.BooleanField(default=False, verbose_name='Опубликовоно')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='doc.category', verbose_name='Категория')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.user', verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['date_creation'],
            },
        ),
    ]
