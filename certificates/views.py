from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from .models import Certificate
from.serializers import CertificateSerializer





@permission_classes([IsAuthenticated])
class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
