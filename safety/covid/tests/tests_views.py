from django.test import TestCase

# Create your tests here.
class TestCovidView(TestCase):
    def test_view_should_be_accessible(self):
        responce = self.client.get('/covid/')
        self.assertEqual(responce.status_code, 200)