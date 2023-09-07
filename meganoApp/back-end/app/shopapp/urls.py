from django.urls import path

from shopapp.orders.orders_api import OrdersApi, OrderApi, paymentApi
from shopapp.cart.cart_api import BasketApi
from shopapp.catalog.catalog_api import (
    ProductApi,
    PopularProductApi,
    TagsApi,
    CategoriesApi,
    LimitedProductApi,
    BannerProductApi,
    ProductReviewApi,
    ProductsApi,
    SaleProductsApi,
)

app_name = "shop_app"


urlpatterns = [
    path("banners", BannerProductApi.as_view()),
    path("categories/", CategoriesApi.as_view(), name="Categories"),
    path("catalog/", ProductsApi.as_view(), name="Catalog"),
    path("products/popular", PopularProductApi.as_view()),
    path("products/limited", LimitedProductApi.as_view()),
    path("sales", SaleProductsApi.as_view(), name="SaleProduct"),
    path("product/<int:id>", ProductApi.as_view(), name="Product"),
    path(
        "product/<int:id>/reviews",
        ProductReviewApi.as_view(),
        name="CreateReview",
    ),
    path("tags", TagsApi.as_view(), name="Tag"),
    path("basket", BasketApi.as_view(), name="Basket"),
    path("orders", OrdersApi.as_view(), name="Orders"),
    path("order/<int:id>", OrderApi.as_view(), name="Order"),
    path("payment/<int:id>", paymentApi),
]
