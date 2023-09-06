from django.http import HttpRequest, HttpResponse
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from shopapp.catalog.catalog_filters import CatalogFilters
from shopapp.catalog.catalog_pagination import CatalogPagination
from shopapp.catalog.catalog_serializers import CategoriesSerializer, TagSerializer, ProductSerializer, SaleProductSerializer
from shopapp.models import Categories, PopularProducts, LimitedProducts, BannersProducts, Product, Tag, SaleProduct


class CategoriesApi(APIView):
    """Отображение категорий"""

    def get(self, request: Request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)


class PopularProductApi(APIView):
    """Отображение популярных продуктов"""

    def get(self, request):
        popularProducts = PopularProducts.objects.first()
        products = popularProducts.items.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class LimitedProductApi(APIView):
    """Отображение лимитированных продуктов"""

    def get(self, request):
        queryset = LimitedProducts.objects.first().items.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class BannerProductApi(APIView):
    """Отображение баннера на главной странице"""

    def get(self, request):
        bannerProducts = BannersProducts.objects.get().items.all()
        serializer = ProductSerializer(bannerProducts, many=True)
        return Response(serializer.data)


class ProductReviewApi(APIView):
    """Создание отзыва о товаре"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: HttpRequest, id):
        data = self.request.data
        product = Product.objects.get(id=id).reviews.create(
            author=data["author"],
            email=data["email"],
            text=data["text"],
            rate=data["rate"],
        )
        product.save()
        return HttpResponse(status=200)


class TagsApi(APIView):
    """Отображение тегов"""

    def get(self, request: HttpRequest):
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)


class ProductApi(APIView):
    """Отображение информации конкретного продукта"""

    def get(self, request: HttpRequest, id):
        print(id)
        product = Product.objects.get(pk=id)
        # product_reviews = ProductReview.objects.filter(product=product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductsApi(ListAPIView):
    """Отображение продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CatalogPagination
    filter_class = CatalogFilters
    filterset_fields = ['title', 'freeDelivery']


class SaleProductsApi(ListAPIView):
    """Продукты со скидкой"""
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer
    pagination_class = CatalogPagination
