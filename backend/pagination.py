from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class PaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
    def get_paginated_response(self, data):
        return Response({
            'results': list(data),
            'total_pages': self.page.paginator.num_pages
        })