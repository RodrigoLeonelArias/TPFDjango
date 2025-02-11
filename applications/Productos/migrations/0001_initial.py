# Generated by Django 3.2 on 2024-07-07 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Preventistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='Marca')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('identificador', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50, verbose_name='Nombre')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de producto')),
                ('cantidad', models.IntegerField(default=0)),
                ('marca', models.ManyToManyField(to='Productos.Marca')),
                ('proveedor', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Preventistas.preventista')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
