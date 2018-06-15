from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import EcomerceSerializer
# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = EcomerceSerializer
