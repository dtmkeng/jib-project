from rest_framework.viewsets import ModelViewSet
from .models import Certificate
from .serializers import CertificateSerializer

# Create your views here.
class CertificateView(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer