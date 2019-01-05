from rest_framework import serializers
from .models import TestimonialModel

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta():
        model = TestimonialModel
        fields = '__all__'
