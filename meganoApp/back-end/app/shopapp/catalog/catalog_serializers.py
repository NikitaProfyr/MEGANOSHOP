from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shopapp.models import CategoriesImage, Subcategories, ProductsImage, Categories, Tag, ProductReview, Product, \
    SaleProduct


class CategoriesImageSerializer(ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = CategoriesImage
        fields = ["src", "alt"]

    def get_src(self, obj):
        return obj.src.url


class SubcategoriesSerializer(ModelSerializer):
    image = CategoriesImageSerializer()

    class Meta:
        model = Subcategories
        fields = ["id", "title", "image"]


class ProductImageSerializer(ModelSerializer):
    src = serializers.SerializerMethodField()

    def get_src(self, obj):
        return obj.src.url

    class Meta:
        model = ProductsImage
        fields = ["src", "alt"]


class CategoriesSerializer(ModelSerializer):
    image = CategoriesImageSerializer()
    subcategories = SubcategoriesSerializer(many=True)

    class Meta:
        model = Categories
        fields = ["id", "title", "image", "subcategories"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        # exclude = ['product']
        fields = "__all__"


class ProductReviewCountSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True)
    tags = TagSerializer(many=True)
    reviews = serializers.SerializerMethodField()

    def get_reviews(self, obj):
        reviews = ProductReview.objects.filter(product=obj.pk).count()
        return reviews

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "rating",
        ]


class ProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True)
    tags = TagSerializer(many=True)
    reviews = ProductReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "rating",
        ]


class SaleProductSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = SaleProduct
        fields = [
            "id",
            "price",
            "salePrice",
            "dateFrom",
            "dateTo",
            "title",
            "images",
        ]
