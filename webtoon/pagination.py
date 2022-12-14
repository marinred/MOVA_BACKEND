from rest_framework.pagination import PageNumberPagination

class WebtoonMPagination(PageNumberPagination):
    page_size = 30