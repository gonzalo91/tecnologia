# Generated by Django 2.2.11 on 2020-04-18 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
                ('latitude', models.CharField(max_length=60)),
                ('longitude', models.CharField(max_length=60)),
                ('times_visited', models.PositiveSmallIntegerField()),
                ('status', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField()),
                ('date_at', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('collection_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.CollectionCenter')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('description_detail', models.CharField(max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
                ('status', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=255)),
                ('image', models.CharField(default='', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('donated', models.BooleanField(default=True)),
                ('type_product', models.CharField(choices=[('p', 'Product'), ('s', 'Service'), ('m', 'Medicine')], max_length=1)),
                ('condition', models.CharField(choices=[('n', 'Nuevo'), ('u', 'Usado')], max_length=1)),
                ('stock', models.PositiveIntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Activo')])),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.ProductCategory')),
                ('collection_center_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.CollectionCenter')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('donated', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('qty', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Web.Product')),
            ],
        ),
    ]
