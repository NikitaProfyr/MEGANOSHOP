from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatalogPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'currentPage'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "items": data,
            "lastPage": self.page.paginator.num_pages,
            "currentPage": self.page.number,
        })
