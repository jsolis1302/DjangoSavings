# Generated by Django 4.2.11 on 2024-04-26 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_alter_accountdetail_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Bank',
        ),
    ]
