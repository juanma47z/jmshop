# Generated by Django 4.2 on 2024-06-21 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre')),
                ('date_register', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=200, verbose_name='nombre producto')),
                ('description', models.TextField(null=True, verbose_name='descripcion')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='precio')),
                ('date_register', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
                ('imagen', models.ImageField(blank=True, upload_to='product')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.category', verbose_name='categoria')),
            ],
        ),
    ]
