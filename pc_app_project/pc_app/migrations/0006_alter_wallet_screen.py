# Generated by Django 4.2.11 on 2024-12-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0005_alter_wallet_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='screen',
            field=models.ImageField(default='Status', upload_to='images'),
        ),
    ]
