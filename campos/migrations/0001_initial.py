# Generated by Django 4.2.4 on 2023-08-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Campo",
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
                (
                    "tipo",
                    models.CharField(
                        choices=[("C", "Caracteres"), ("D", "Decimal"), ("T", "Texto")],
                        max_length=1,
                    ),
                ),
                ("tabela", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MyModel",
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
                ("descricao", models.CharField(max_length=50)),
            ],
        ),
    ]
