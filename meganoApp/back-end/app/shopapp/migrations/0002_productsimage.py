# Generated by Django 4.0.6 on 2023-08-31 21:49

from django.db import migrations, models
import shopapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to=shopapp.models.load_to_image_products, verbose_name='Ссылка')),
                ('alt', models.CharField(max_length=128, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Изображение продукта',
                'verbose_name_plural': 'Изображения продуктов',
            },
        ),
    ]
