# Generated by Django 4.0 on 2021-12-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_tb_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_tb',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
