from rest_framework.pagination import PageNumberPagination


class BoardPagination(PageNumberPagination):
    page_size = 10
    
class WebtoonPagination(PageNumberPagination):
    page_size = 20