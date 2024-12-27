# Generated by Django 5.0 on 2024-12-27 07:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=15, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarLocationHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentacar.car')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('place_of_order', models.CharField(max_length=255)),
                ('place_of_return', models.CharField(max_length=255)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentacar.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_start', models.DateTimeField()),
                ('rental_end', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentacar.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
