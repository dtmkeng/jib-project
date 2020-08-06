import json

from django.views import View
from django.http import HttpResponse
from .models import Worker
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView


class WorkerSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    is_available = serializers.BooleanField()
    primary_phone = serializers.CharField()
    secondary_phone = serializers.CharField()
    address = serializers.CharField()
    
# class base view
class WorkerListView(APIView):
    def get(self, request):
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)

    