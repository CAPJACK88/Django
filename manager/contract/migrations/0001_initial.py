# Generated by Django 3.2.3 on 2021-06-01 10:12

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cont', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=255, unique=True, verbose_name='Номер')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('comment', django_ckeditor_5.fields.CKEditor5Field(blank=True, max_length=1000, verbose_name='Комментарий')),
                ('submitted', models.BooleanField(default=False, verbose_name='Отправлен')),
                ('publications', models.BooleanField(default=True, verbose_name='Опубликовоно')),
                ('company', models.ManyToManyField(blank=True, to='cont.Company', verbose_name='Компания')),
                ('fixed', models.ManyToManyField(blank=True, to='user.User', verbose_name='Закреплено')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договоры',
                'ordering': ['-date_creation'],
            },
        ),
    ]
