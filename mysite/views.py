

from django.shortcuts import render
from rest_framework import viewsets
from backend.serializers import ProjectSerializer
from backend.models import Project

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()