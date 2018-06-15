from rest_framework import serializers
from .models import Category

class EcomerceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields =('id','name','description')