# Generated by Django 4.0 on 2021-12-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_admin_signup'),
    ]

    operations = [
        migrations.CreateModel(
            name='tables_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usercourier')),
            ],
        ),
    ]
