from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TestimonialModel
from .serializer import TestimonialSerializer
# Create your views here.
class TestiView(APIView):
    def get(self,request):
        db_data = TestimonialModel.objects.all()
        ser_data = TestimonialSerializer(db_data,many=True)
        return Response(ser_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        ser_data = TestimonialSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(ser_data.data,status=status.HTTP_400_BAD_REQUEST)           

