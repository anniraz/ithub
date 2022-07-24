from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import User

from rest_framework.pagination import PageNumberPagination

class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    username=CharFilterInFilter(field_name='username',lookup_expr='in')
    # category=CharFilterInFilter(field_name='category__title',lookup_expr='in')

    class Meta:
        model=User
        fields=['username']


class Paginations(PageNumberPagination):
    page_size=12
    max_page_size=1000

    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
            },
            'count':self.page.paginator.count,
            'results':data
        })