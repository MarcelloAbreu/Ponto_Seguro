# Generated by Django 4.1.7 on 2023-05-27 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_remove_histregistro_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horaextra',
            name='sitApr',
        ),
        migrations.AddField(
            model_name='horaextra',
            name='altEnt1',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='horaextra',
            name='altEnt3',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='horaextra',
            name='altSai2',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='horaextra',
            name='altSai4',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='horaextra',
            name='sitAPR',
            field=models.CharField(default='PEN', max_length=3),
        ),
    ]
