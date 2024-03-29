# Generated by Django 5.0.1 on 2024-02-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryManagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('composition', models.CharField(default='ok', max_length=122)),
                ('quantity', models.CharField(max_length=122)),
                ('price', models.CharField(max_length=122)),
                ('date', models.DateField()),
                ('exp_date', models.DateField(default='2024-02-07')),
                ('mfg_date', models.DateField(default='2024-02-07')),
            ],
        ),
    ]
