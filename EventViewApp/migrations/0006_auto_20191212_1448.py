# Generated by Django 2.1 on 2019-12-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventViewApp', '0005_espaciootro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='prestadorServicio',
            field=models.TextField(max_length=45, verbose_name='prestador'),
        ),
    ]
