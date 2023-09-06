# Generated by Django 4.0.6 on 2023-08-31 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0006_productreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name': 'Отзывы о товарах', 'verbose_name_plural': 'Отзывы о товарах'},
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='дата создания'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='цена продукта')),
                ('count', models.IntegerField(blank=True, default=0, null=True, verbose_name='количество')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('title', models.CharField(default='', max_length=50, verbose_name='заголовок продукта')),
                ('description', models.TextField(max_length=300, verbose_name='описание товара')),
                ('freeDelivery', models.BooleanField(default=False)),
                ('avaible', models.BooleanField(default=False)),
                ('rating', models.FloatField(default=0, verbose_name='рейтинг')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopapp.categories')),
                ('images', models.ManyToManyField(null=True, to='shopapp.productsimage')),
                ('reviews', models.ManyToManyField(null=True, to='shopapp.productreview')),
                ('tags', models.ManyToManyField(null=True, to='shopapp.tag')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
