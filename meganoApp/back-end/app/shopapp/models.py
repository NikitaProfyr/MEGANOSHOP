from django.db import models

from userapp.models import Profile


def load_to_image_categories(instance: "Categories", filename: str) -> str:
    """Функция для загрузки изображений категорий"""
    return f"categories/categories_{instance.pk}/image_{filename}"


def load_to_image_products(instance: "Product", filename: str) -> str:
    """Функция для загрузки изображений продекта"""
    return f"product/product_{instance.pk}/image_{filename}"


# Create your models here.


class CategoriesImage(models.Model):
    src = models.ImageField(
        upload_to=load_to_image_categories,
        verbose_name="Ссылка",
    )
    alt = models.CharField(max_length=128, verbose_name="Описание")

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = "Изображение категории"
        verbose_name_plural = "Изображения категорий"


class ProductsImage(models.Model):
    src = models.ImageField(
        upload_to=load_to_image_products,
        verbose_name="Ссылка",
    )
    alt = models.CharField(max_length=128, verbose_name="Описание")

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = "Изображение продукта"
        verbose_name_plural = "Изображения продуктов"


class Subcategories(models.Model):
    title = models.CharField(max_length=50, verbose_name="наименование категории")
    image = models.ForeignKey(CategoriesImage, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Подкатегории"
        verbose_name_plural = "Подкатегории"


class Categories(models.Model):
    title = models.CharField(max_length=50, verbose_name="наименование категории")
    image = models.ForeignKey(CategoriesImage, on_delete=models.CASCADE, null=True)
    subcategories = models.ManyToManyField(Subcategories, null=True)

    # subcategories = models.ForeignKey(Subcategories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name="наименование тега")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэги"
        verbose_name_plural = "Тэги"


class ProductReview(models.Model):
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    author = models.CharField(max_length=150, null=True, verbose_name="Автор")
    email = models.CharField(max_length=100, null=True, verbose_name="Эл. почта")
    text = models.TextField(max_length=300, verbose_name="текст отзыва")
    rate = models.IntegerField(null=True, verbose_name="оценка")
    date = models.DateField(
        null=True, blank=True, auto_now_add=True, verbose_name="дата создания"
    )

    class Meta:
        verbose_name = "Отзывы о товарах"
        verbose_name_plural = "Отзывы о товарах"


class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, verbose_name="цена продукта"
    )
    count = models.IntegerField(
        default=0, null=True, blank=True, verbose_name="количество"
    )
    date = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(
        max_length=50, default="", verbose_name="заголовок продукта"
    )
    description = models.TextField(max_length=300, verbose_name="описание товара")
    freeDelivery = models.BooleanField(default=False)
    images = models.ManyToManyField(ProductsImage, null=True)
    tags = models.ManyToManyField(Tag, null=True)
    avaible = models.BooleanField(default=False)
    # reviews = models.IntegerField(default=0, verbose_name="ревью")
    reviews = models.ManyToManyField(ProductReview, null=True, blank=True)
    rating = models.FloatField(default=0, verbose_name="рейтинг")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукты"
        verbose_name_plural = "Продукты"


class Order(models.Model):
    createdAt = models.DateField(null=True, blank=True, verbose_name="дата создания")
    fullName = models.CharField(max_length=100, null=True, verbose_name="ФИО")
    email = models.CharField(max_length=100, null=True, verbose_name="Эл. почта")
    phone = models.CharField(max_length=12, null=True, verbose_name="Номер телефона")
    deliveryType = models.CharField(
        max_length=20, null=True, verbose_name="Тип доставки"
    )
    paymentType = models.CharField(max_length=20, null=True, verbose_name="Тип платежа")
    totalCost = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    status = models.CharField(max_length=20, null=True, verbose_name="статус заказа")
    city = models.CharField(
        max_length=100, null=True, verbose_name="Город доставки заказа"
    )
    address = models.TextField(
        max_length=150, null=True, blank=True, verbose_name="адрес заказа"
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class PopularProducts(models.Model):
    items = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Популярные продукты"
        verbose_name_plural = "Популярные продукты"

    def __str__(self):
        return f"Популярные продукты"


class LimitedProducts(models.Model):
    items = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Лимитированный продукт"
        verbose_name_plural = "Лимитированные продукты"

    def __str__(self):
        return f"Лимитированные продукты"


class BannersProducts(models.Model):
    items = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннер"

    def __str__(self):
        return f"Баннер"


class SaleProduct(models.Model):
    price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0, verbose_name="цена продукта"
    )
    salePrice = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        verbose_name="скидочная цена продукта",
    )
    dateFrom = models.DateField(auto_now_add=True, null=True)
    dateTo = models.DateField(null=True)
    title = models.CharField(
        max_length=50, default="", verbose_name="заголовок продукта"
    )
    images = models.ManyToManyField(ProductsImage, null=True)

    class Meta:
        verbose_name = "Товар со скидкой"
        verbose_name_plural = "Товары со скидкой"

    def __str__(self):
        return f"Акционный товар {self.title}"
