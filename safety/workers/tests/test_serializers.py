from django.test import TestCase
from ..serializers import WorkerSerializer
from ..models import Worker


class TestSerializer(TestCase):
    def test_serializer_should_return_correct_serialized_data(self):
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

        serializer = WorkerSerializer(worker)

        expected = {
            'first_name': first_name,
            'last_name': last_name,
            'is_available': is_available,
            'primary_phone': primary_phone,
            'secondary_phone': secondary_phone,
            'address': address,
        }

        assert serializer.data == expected
