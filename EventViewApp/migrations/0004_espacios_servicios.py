# Generated by Django 2.1 on 2019-12-12 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventViewApp', '0003_evento_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='espacios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre:')),
                ('casaEventos', models.TextField(max_length=45)),
                ('descripcion', models.TextField(max_length=45)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='servicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre:')),
                ('prestadorServicio', models.TextField(max_length=45)),
                ('descripcion', models.TextField(max_length=45)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
