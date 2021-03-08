from rest_framework import serializers
from .models import Admission

class admissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admission
        fields=['name','phone','city','amount']