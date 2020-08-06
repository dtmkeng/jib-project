from django.test import TestCase
from ..models import Worker
import json

class TestWorkerListView(TestCase):
    def test_view_should_be_accessible(self):
        result = self.client.get('/workers/')
        self.assertEqual(result.status_code ,200)
        
    def test_view_should_render_list_of_worker_name(self):
        # Given
        Worker.objects.create(
            first_name = 'first_name',
            last_name = 'last_name',
            is_available = True,
            primary_phone = 'primary_phone',
            secondary_phone = 'secondary_phone',
            address = 'address',
        )
        Worker.objects.create(
            first_name = 'first_name1',
            last_name = 'last_name1',
            is_available = True,
            primary_phone = 'primary_phone1',
            secondary_phone = 'secondary_phone1',
            address = 'address1',
        )
        
        #When
        response = self.client.get('/workers/')
        
        #Then
        # self.assertContains(response, '<li>first_name</li>')
        # self.assertContains(response, '<li>first_name1</li>')
        
        worker_list = [
            {
                'first_name': 'first_name',
                'last_name': 'last_name',
                'is_available': True,
                'primary_phone': 'primary_phone',
                'secondary_phone': 'secondary_phone',
                'address': 'address',
            },
             {
                'first_name': 'first_name1',
                'last_name': 'last_name1',
                'is_available': True,
                'primary_phone': 'primary_phone1',
                'secondary_phone': 'secondary_phone1',
                'address': 'address1',
            },
        ]
        
        self.assertEqual(response.content.decode('utf-8'), json.dumps(worker_list))
        