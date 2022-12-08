from rest_framework import serializers
from rest_framework.views import APIView

from category.models import Category

class categoryView(serializers.ModelSerializer):

    class Meta:

        model = Category
        fields = (
            '__all__'
        )