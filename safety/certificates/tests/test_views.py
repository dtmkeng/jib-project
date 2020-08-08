# import json
from django.test import TestCase
from ..serializers import CertificateSerializer
from ..models import Certificate
from ..views import CertificateView


class TestWorkerListView(TestCase):
    def test_view_should_be_accessible(self):
        response = self.client.get('/certificates/')
        assert response.status_code == 200

    def test_models_view_set_should_set_queryset(self):
        assert list(CertificateView.queryset) == list(Certificate.objects.all())
    
    def test_model_view_set_should_set_serializer_class(self):
        assert CertificateView.serializer_class == CertificateSerializer