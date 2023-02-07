# Generated by Django 4.1.4 on 2023-02-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Aron", "0002_delete_events"),
    ]

    operations = [
        migrations.CreateModel(
            name="Events",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_event", models.CharField(max_length=200, null=True)),
                ("Date", models.DateTimeField(auto_now_add=True, null=True)),
                ("Description", models.CharField(max_length=1000, null=True)),
                ("Attendee", models.IntegerField(blank=True)),
            ],
        ),
    ]