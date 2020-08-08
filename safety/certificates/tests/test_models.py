from django.test import TestCase
from ..models import Certificate
from workers.models import Worker


class TestWorkers(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_worker_should_have_define_fields(_):
        # Given
        name = 'JS Certificat by ODDS'
        issued_by = 'ODDS ProoF'
        
        
        worker = Worker.objects.create(
            first_name='first_name',
            last_name='last_name',
            is_available=True,
            primary_phone='primary_phone',
            secondary_phone='secondary_phone',
            address='address',
        )
        
        # When
        certificate = Certificate.objects.create(
            name=name,
            issued_by=issued_by,
            worker=worker,
        )
        # Then
        assert certificate.name == name
        assert certificate.issued_by == issued_by
        assert certificate.worker == worker
