from django.shortcuts import render
from .serializer import ImageProgramSerilizers
from .models import ImagePro
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageProgramSerilizers
    queryset = ImagePro.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


