# Generated by Django 4.1.5 on 2023-02-01 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playspots_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=25)),
                ("phone_no", models.CharField(max_length=10)),
            ],
        ),
    ]
