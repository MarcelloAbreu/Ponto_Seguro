# Generated by Django 4.1.7 on 2023-03-26 20:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dt_troca_senha',
            field=models.DateField(verbose_name=django.utils.timezone.now),
        ),
    ]
