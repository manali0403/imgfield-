from rest_framework import serializers
from .models import ImagePro


class ImageProgramSerilizers(serializers.ModelSerializer):
    class Meta:
        model = ImagePro
        fields = '__all__'
        