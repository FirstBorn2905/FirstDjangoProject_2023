# Generated by Django 4.2.5 on 2023-10-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_reporteventas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporteventas',
            name='fecha',
        ),
        migrations.AddField(
            model_name='reporteventas',
            name='mes',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
