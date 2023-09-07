from _decimal import Decimal

from django.conf import settings
from django.http import HttpRequest

from shopapp.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: Product, quantity=1, updateQuantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        productId = str(product.id)

        if productId not in self.cart:
            self.cart[productId] = {"quantity": 0, "price": str(product.price)}
        if updateQuantity:
            self.cart[productId]["quantity"] = quantity
        else:
            self.cart[productId]["quantity"] += quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product: Product):
        productId = str(product.id)

        if productId in self.cart:
            del self.cart[productId]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(
            Decimal(item["price"]) * item["quantity"] for item in self.cart.values()
        )

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_cart_data(self):
        # Получение данных о продуктах из базы данных
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
