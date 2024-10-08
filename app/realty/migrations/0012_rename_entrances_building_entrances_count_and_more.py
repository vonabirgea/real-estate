# Generated by Django 5.1.1 on 2024-10-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0011_building_address_project_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='entrances',
            new_name='entrances_count',
        ),
        migrations.RenameField(
            model_name='entrance',
            old_name='total_flats',
            new_name='flats_count',
        ),
        migrations.RenameField(
            model_name='entrance',
            old_name='total_floors',
            new_name='floors_count',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='total_buildings',
            new_name='buildings_count',
        ),
        migrations.RemoveField(
            model_name='floor',
            name='flats_on_floor',
        ),
        migrations.AddField(
            model_name='floor',
            name='flats_count',
            field=models.IntegerField(null=True, verbose_name='Число квартир на этаже'),
        ),
    ]