from django.test import TestCase
from ..serializers import CertificateSerializer
from ..models import Certificate


class TestCertificateModelSerializer(TestCase):
    def test_model_serializer_shuld_set_certificate_model(self):
        assert CertificateSerializer.Meta.model == Certificate