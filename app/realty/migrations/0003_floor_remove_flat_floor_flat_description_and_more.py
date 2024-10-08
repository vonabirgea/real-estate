# Generated by Django 5.1.1 on 2024-09-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0002_alter_flat_rooms_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('floor', models.IntegerField(verbose_name='Этаж')),
                ('flats_count', models.IntegerField(verbose_name='Количество квартир на этаже')),
                ('status', models.CharField(choices=[('FRE', 'Полностью свободен'), ('PRT', 'Частично занят'), ('SLD', 'Полностью выкуплен')], default='FRE', max_length=3, verbose_name='Статус')),
                ('description', models.TextField(blank=True, verbose_name='Описание этажа')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='flat',
            name='floor',
        ),
        migrations.AddField(
            model_name='flat',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание квартиры'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления'),
        ),
    ]
