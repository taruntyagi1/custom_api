from products.models import Variants
from rest_framework import serializers
from rest_framework.views import APIView



class variantView(serializers.ModelSerializer):

    class Meta:
        model = Variants
        fields = (
            '__all__'
        )