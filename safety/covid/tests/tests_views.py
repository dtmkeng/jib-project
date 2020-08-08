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
        
    @patch('covid.views.requests.get')
    def test_view_shoud_render_number_of_confirmed(self, mock):
        r = mock.return_value
        r.json.return_value = {
            'Confirmed': 3345,
            'Recovered': 3148,
            'Hospitalized': 139,
            'Deaths': 58,
            'NewConfirmed': 50,
            'NewRecovered': 0,
            'NewHospitalized': 15,
            'NewDeaths': 0,
            'UpdateDate': "07/08/2020 11:36",
            'Source': "https://covid19.th-stat.com/",
            'DevBy': "https://www.kidkarnmai.com/",
            'SeverBy': "https://smilehost.asia/"
        }
            
        responce = self.client.get('/covid/')

        self.assertContains(responce, 'NewConfirmed: 50')