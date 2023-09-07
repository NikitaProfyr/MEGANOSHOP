# Generated by Django 4.0.6 on 2023-09-02 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("userapp", "0001_initial"),
        ("shopapp", "0013_alter_order_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="userapp.profile"
            ),
        ),
    ]
