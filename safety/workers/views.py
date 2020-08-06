from django.views import View
from django.http import HttpResponse
from .models import Worker
from django.shortcuts import render
import json

# class base view
class WorkerListView(View):
    def get(self, request):
        workers = Worker.objects.all()
        
        # html = ''
        # for worker in workers:
        #     html += f'<li>{worker.first_name}</li>'
        
        worker_list = []
        for worker in workers:
            d = {
                'first_name': worker.first_name,
                'last_name': worker.last_name,
                'is_available': worker.is_available,
                'primary_phone': worker.primary_phone,
                'secondary_phone': worker.secondary_phone,
                'address': worker.address,
            }
            worker_list.append(d)
        
        return HttpResponse(
            json.dumps(worker_list),
            content_type='application/json',
        )
    