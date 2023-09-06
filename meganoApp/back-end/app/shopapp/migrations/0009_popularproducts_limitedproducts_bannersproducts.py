# Generated by Django 4.0.6 on 2023-08-31 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0008_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='shopapp.product')),
            ],
            options={
                'verbose_name': 'Популярные продукты',
                'verbose_name_plural': 'Популярные продукты',
            },
        ),
        migrations.CreateModel(
            name='LimitedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='shopapp.product')),
            ],
            options={
                'verbose_name': 'Лимитированный продукт',
                'verbose_name_plural': 'Лимитированные продукты',
            },
        ),
        migrations.CreateModel(
            name='BannersProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='shopapp.product')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннер',
            },
        ),
    ]
