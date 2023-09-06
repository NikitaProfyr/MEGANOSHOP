from rest_framework.serializers import ModelSerializer

from shopapp.catalog.catalog_serializers import ProductReviewCountSerializer
from shopapp.models import Order


class OrderSerializer(ModelSerializer):
    products = ProductReviewCountSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "createdAt",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "products",
        ]
