from django.test import TestCase
from ..models import Worker


class TestWorkers(TestCase):
    def test_worker_should_have_define_fields(self):
        # Given
        first_name = 'Keng'
        last_name = 'Mark'
        is_available = True
        primary_phone = '081-669-777x'
        secondary_phone = '092-009-000x'
        address = 'Geeky Bass All Start'
        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )
        # Then
        self.assertEqual(worker.first_name, first_name)
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.is_available, is_available)
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)
