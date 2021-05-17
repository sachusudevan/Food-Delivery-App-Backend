from django.shortcuts import render
from rest_framework import status
from apps.users.models import Users
from apps.products.models import Category
from apps.products.serializers import CategorySerializer

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.settings import BASE_URL

class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    
    def get(self, *args, **kwargs):
        category =  Category.objects.filter(is_publish=1)
        categoryserializer = CategorySerializer(category, many=True)
        if len(categoryserializer.data) != 0:
            response = {
                'code': status.HTTP_200_OK,
                'BASE_URL': BASE_URL,
                'data': categoryserializer.data
            }
            return Response(response)
        else:
            response = {
                'code': status.HTTP_200_OK,
                'BASE_URL': BASE_URL,
                'data': {}
            }
            return Response(response)