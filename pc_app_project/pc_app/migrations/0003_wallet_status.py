# Generated by Django 4.2.11 on 2024-12-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0002_alter_wallet_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='status',
            field=models.CharField(default='Status', max_length=500),
        ),
    ]
