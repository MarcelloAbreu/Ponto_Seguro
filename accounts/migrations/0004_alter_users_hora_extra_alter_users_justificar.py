# Generated by Django 4.1.7 on 2023-04-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_users_hora_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='hora_extra',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='justificar',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]