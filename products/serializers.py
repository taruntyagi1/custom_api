from rest_framework import serializers
from products.models import Products
from rest_framework.views import APIView
from my_api.serializers import variantView
from category.serializers import categoryView
from variants.serializers import variantsserializer




class Productserializer(serializers.ModelSerializer):
    variants = variantsserializer()
    category =  categoryView()
    class Meta:

        model  = Products
        fields = (
            'id',
            'product_name',
            'slug',
            'price',
            'stock',
            'image',
            'is_available',
            'variants',
            'category'

        )



class productcreate(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = (
         
            'slug',
            'price',
            'stock'
            
        )