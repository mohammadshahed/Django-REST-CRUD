from rest_framework import viewsets

from .serializers import admissionSerializer
from .models import Admission


class AdmissionViewset(viewsets.ModelViewSet):
    queryset=Admission.objects.all()
    serializer_class=admissionSerializer