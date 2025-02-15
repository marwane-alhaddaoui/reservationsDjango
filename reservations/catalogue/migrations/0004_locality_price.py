# Generated by Django 5.1.2 on 2025-02-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(max_length=6)),
                ('locality', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'localities',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=255)),
                ('start_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'prices',
            },
        ),
    ]
