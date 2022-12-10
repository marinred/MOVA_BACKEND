from rest_framework.pagination import PageNumberPagination


class NoticePagination(PageNumberPagination):
    page_size = 10