# Generated by Django 4.2.11 on 2024-04-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_account_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AccountMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
