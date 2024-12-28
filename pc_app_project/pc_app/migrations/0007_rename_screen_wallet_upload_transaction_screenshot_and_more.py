# Generated by Django 4.2.11 on 2024-12-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pc_app', '0006_alter_wallet_screen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='screen',
            new_name='Upload_transaction_screenshot',
        ),
        migrations.RemoveField(
            model_name='pc_store',
            name='Processor',
        ),
        migrations.RemoveField(
            model_name='pc_store',
            name='RAM',
        ),
        migrations.RemoveField(
            model_name='pc_store',
            name='img4',
        ),
        migrations.AlterField(
            model_name='wallet',
            name='Deposit_amount',
            field=models.CharField(default='No payment fund yet', max_length=500),
        ),
    ]