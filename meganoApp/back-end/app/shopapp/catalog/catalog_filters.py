from django_filters import FilterSet, filters

from shopapp.models import Product


class CatalogFilters(FilterSet):
    name = filters.CharFilter(field_name='title', lookup_expr='icontains')
    minPrice = filters.NumberFilter(field_name='price', lookup_expr='gte')
    maxPrice = filters.NumberFilter(field_name='price', lookup_expr='lte')
    freeDelivery = filters.BooleanFilter(field_name='freeDelivery')
    available = filters.BooleanFilter(field_name='available')

    class Meta:
        model = Product
        fields = []
