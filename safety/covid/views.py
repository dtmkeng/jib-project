from django.views import View
from django.http import HttpResponse
import requests

# Create your views here.
class CovidView(View):
    def get(self, request):
        res = requests.get('https://covid19.th-stat.com/api/open/today')
        data = res.json()
        new_confirmed = data['NewConfirmed']
        return HttpResponse(f'NewConfirmed: {new_confirmed}')
