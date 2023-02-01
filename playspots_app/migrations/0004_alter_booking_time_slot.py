# Generated by Django 4.1.5 on 2023-02-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("playspots_app", "0003_alter_user_id_alter_venue_id_booking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="time_slot",
            field=models.CharField(
                choices=[
                    ("4PM", "4PM"),
                    ("5PM", "5PM"),
                    ("6PM", "6PM"),
                    ("7PM", "7PM"),
                    ("8PM", "8PM"),
                    ("9PM", "9PM"),
                    ("10PM", "10PM"),
                    ("11PM", "11PM"),
                ],
                max_length=25,
            ),
        ),
    ]