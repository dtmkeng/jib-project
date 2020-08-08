from django.test import TestCase
from ..serializers import CertificateSerializer
from ..models import Certificate


class TestCertificateModelSerializer(TestCase):
    def test_model_serializer_should_set_certificate_model(self):
        assert CertificateSerializer.Meta.model == Certificate
    
    def test_model_serializer_should_use_all_fields(self):
        assert CertificateSerializer.Meta.fields == '__all__'