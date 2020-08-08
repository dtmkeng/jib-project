import os
from unittest.mock import MagicMock
from django.core.files import File
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

        image_mock = MagicMock(spec=File)
        image_mock.name = 'keng.png'

        # When
        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
            image_proflie=image_mock
        )
        # Then
        self.assertEqual(worker.first_name, first_name)
        assert worker.first_name == first_name  # use assert pytest
        self.assertEqual(worker.last_name, last_name)
        self.assertEqual(worker.is_available, is_available)
        assert worker.is_available is is_available  # use assert pytest
        self.assertEqual(worker.primary_phone, primary_phone)
        self.assertEqual(worker.secondary_phone, secondary_phone)
        self.assertEqual(worker.address, address)
        self.assertEqual(worker.image_proflie.name, image_mock.name)

        os.remove('media/keng.png')

    def test_model_should_have_friendly_name(self):
        first_name = 'Keng'
        last_name = 'Mak'
        is_available = True
        primary_phone = '081-689-777x'
        secondary_phone = '081-689-778x'
        address = 'Geeky Base All Stars'

        worker = Worker.objects.create(
            first_name=first_name,
            last_name=last_name,
            is_available=is_available,
            primary_phone=primary_phone,
            secondary_phone=secondary_phone,
            address=address,
        )

        assert worker.__str__() == f'{first_name} {last_name}'
