# import json

# from django.views import View
# from django.http import HttpResponse
from .models import Worker
from .serializers import WorkerSerializer
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# class base view
class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

# from rest_framework import viewsets

# class WorkerListViewSetView(viewsets.ModelViewSet):
#     queryset = Worker.objects.all()
#     serializer_class = WorkerSerializer
