# Generated by Django 4.2.5 on 2023-10-10 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_reporteventas_showganancia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporteventas',
            name='showGanancia',
        ),
    ]
