# Generated by Django 4.0 on 2021-12-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_tb_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=50)),
                ('lastname', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('gender', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
                ('confirmpassword', models.CharField(default='', max_length=100)),
            ],
        ),
    ]