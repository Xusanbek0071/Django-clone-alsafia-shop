# Generated by Django 3.2.12 on 2022-04-17 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='mahsulotning nomi')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
                ('price', models.FloatField(verbose_name='mahsulotning narxi')),
                ('discount', models.PositiveIntegerField(blank=True, default=0, verbose_name='Chegirma')),
                ('image_450_200', models.ImageField(blank=True, default='default/banner-1.jpg', upload_to='', verbose_name='450x200')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.categories')),
            ],
        ),
    ]
