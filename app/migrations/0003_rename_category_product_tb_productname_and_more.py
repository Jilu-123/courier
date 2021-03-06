# Generated by Django 4.0 on 2021-12-20 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product_tb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_tb',
            old_name='category',
            new_name='productname',
        ),
        migrations.RemoveField(
            model_name='product_tb',
            name='details',
        ),
        migrations.RemoveField(
            model_name='product_tb',
            name='fileupload',
        ),
        migrations.RemoveField(
            model_name='product_tb',
            name='name',
        ),
        migrations.AddField(
            model_name='product_tb',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product_tb',
            name='destination',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product_tb',
            name='starting',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product_tb',
            name='price',
            field=models.CharField(default='', max_length=50),
        ),
    ]
