# Generated by Django 4.2.11 on 2024-04-26 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0009_delete_account_delete_bank'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountMaster',
            new_name='Account',
        ),
    ]
