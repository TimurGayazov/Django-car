# Generated by Django 5.0.4 on 2024-04-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordmaintenance',
            name='record_maintenance_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
