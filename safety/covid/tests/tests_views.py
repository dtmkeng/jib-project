from django.test import TestCase
from unittest.mock import patch

# Create your tests here.
class TestCovidView(TestCase):
    @patch('covid.views.requests.get')
    def test_view_should_be_accessible(self, _):
        responce = self.client.get('/covid/')
        self.assertEqual(responce.status_code, 200)
    
    @patch('covid.views.requests.get')
    def test_view_should_call_covid_api(self, mock):
        self.client.get('/covid/')
        mock.assert_called_once_with('https://covid19.th-stat.com/api/open/today')