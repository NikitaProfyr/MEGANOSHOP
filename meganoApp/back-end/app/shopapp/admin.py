from django.contrib import admin

from shopapp.models import (
    Product,
    Order,
    Categories,
    ProductReview,
    CategoriesImage,
    ProductsImage,
    Tag,
    Subcategories,
    SaleProduct,
    PopularProducts,
    LimitedProducts,
    BannersProducts,
)


# Register your models here.


@admin.register(CategoriesImage)
class CategoriesImageModelAdmin(admin.ModelAdmin):
    model = CategoriesImage


@admin.register(ProductsImage)
class ProductsImageModelAdmin(admin.ModelAdmin):
    model = ProductsImage


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    model = Product


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    model = Order


@admin.register(Categories)
class CategoriesModelAdmin(admin.ModelAdmin):
    model = Categories


@admin.register(Subcategories)
class SubcategoriesModelAdmin(admin.ModelAdmin):
    model = Subcategories


@admin.register(ProductReview)
class ProductReviewModelAdmin(admin.ModelAdmin):
    model = ProductReview


@admin.register(SaleProduct)
class SaleProductModelAdmin(admin.ModelAdmin):
    model = SaleProduct


@admin.register(PopularProducts)
class PopularProductsModelAdmin(admin.ModelAdmin):
    model = PopularProducts


@admin.register(LimitedProducts)
class LimitedProductsModelAdmin(admin.ModelAdmin):
    model = LimitedProducts


@admin.register(BannersProducts)
class BannersProductsModelAdmin(admin.ModelAdmin):
    model = BannersProducts
