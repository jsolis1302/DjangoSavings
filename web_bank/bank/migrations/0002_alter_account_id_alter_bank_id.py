# Generated by Django 4.2.11 on 2024-04-08 05:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bank", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="bank",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
