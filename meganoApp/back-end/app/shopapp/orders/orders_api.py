from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from shopapp.cart.cart import Cart
from shopapp.catalog.catalog_serializers import ProductReviewCountSerializer
from shopapp.orders.orders_serializers import OrderSerializer
from userapp.models import Profile
from shopapp.models import Order


class OrdersApi(APIView):
    """Отображение заказов"""
    def get(self, request: HttpRequest):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        order = Order.objects.filter(user=profile).all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest):
        cart = Cart(self.request)
        user = self.request.user.id
        products = cart.get_cart_data()
        profile = Profile.objects.get(user=user)
        order = Order.objects.create(user=profile)
        for product in products:
            order.products.add(product)
        order.save()
        response = {"orderId": order.id}
        return Response(response)


class OrderApi(APIView):
    """Отображение информации о конкретном заказе"""
    def get(self, request, id):
        order = Order.objects.get(pk=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = OrderSerializer(data=self.request.data)
        if serializer.is_valid():
            order = Order.objects.get(pk=id)
            order.fullName = serializer.validated_data["fullName"]
            order.phone = serializer.validated_data["phone"]
            order.email = serializer.validated_data["email"]
            order.deliveryType = serializer.validated_data["deliveryType"]
            order.city = serializer.validated_data["city"]
            order.address = serializer.validated_data["address"]
            order.paymentType = serializer.validated_data["paymentType"]
            order.save()
            data = {"orderId": order.pk}
            return JsonResponse(data)
        else:
            # Данные формы невалидны, вернуть ошибку
            return Response(serializer.errors, status=400)


def paymentApi(request, id):
    print("qweqwewqeqwe", id)
    cart = Cart(request)
    produscts = cart.get_cart_data()
    for item in produscts:
        cart.remove(item)
    cart.save()
    return HttpResponse(status=200)
