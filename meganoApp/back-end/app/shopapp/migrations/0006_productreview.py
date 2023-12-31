# Generated by Django 4.0.6 on 2023-08-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0005_tag"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductReview",
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
                    "author",
                    models.CharField(max_length=150, null=True, verbose_name="Автор"),
                ),
                (
                    "email",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Эл. почта"
                    ),
                ),
                ("text", models.TextField(max_length=300, verbose_name="текст отзыва")),
                ("rate", models.IntegerField(null=True, verbose_name="оценка")),
                (
                    "date",
                    models.DateField(
                        blank=True, null=True, verbose_name="дата создания"
                    ),
                ),
            ],
        ),
    ]
