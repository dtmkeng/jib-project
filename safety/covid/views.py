from django.views import View
from django.http import HttpResponse

# Create your views here.
class CovidView(View):
    def get(self, request):
        return HttpResponse()
