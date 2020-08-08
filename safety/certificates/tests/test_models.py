from django.test import TestCase
from ..models import Certificate


class TestWorkers(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_worker_should_have_define_fields(_):
        # Given
        name = 'JS Certificat by ODDS'
        issued_by = 'ODDS ProoF'
        
        # When
        worker = Certificate.objects.create(
            name=name,
            issued_by=issued_by,
        )
        # Then
        assert worker.name == name
        assert worker.issued_by == issued_by
