from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shopapp.cart.cart import Cart
from shopapp.catalog.catalog_serializers import ProductSerializer
from shopapp.models import Product


class BasketApi(APIView):
    """Работа с корзиной"""

    def get(self, request):
        """Отображение продуктов корзины"""
        cart = Cart(request)
        products = cart.get_cart_data()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest):
        """Отправка продукта в корзину"""
        data = self.request.data
        product = Product.objects.get(pk=int(data["id"]))
        cart = Cart(request)
        print(data["count"])
        cart.add(product, data["count"])
        cart.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request: HttpRequest):
        """Удаление продукта из корзины"""
        data = self.request.data
        cart = Cart(request)
        product = Product.objects.get(pk=int(data["id"]))
        cart.remove(product)
        cart.save()
        return Response(status=200)
