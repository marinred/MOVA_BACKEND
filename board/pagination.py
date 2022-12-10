from rest_framework.pagination import PageNumberPagination


class BoardPagination(PageNumberPagination):
    page_size = 10