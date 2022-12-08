from rest_framework import serializers
from variants.models import Variants


class variantsserializer(serializers.ModelSerializer):

    class Meta:
        model = Variants
        fields = (
            '__all__'
        )