# Generated by Django 4.0.6 on 2023-01-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
