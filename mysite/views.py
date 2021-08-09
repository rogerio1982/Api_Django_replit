

from django.shortcuts import render
from rest_framework import viewsets
from backend.serializers import ProjectSerializer
from backend.serializers import MarvelSerializer
from backend.models import Project
from backend.models import Marvel
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TodoView2(viewsets.ModelViewSet):
    serializer_class = MarvelSerializer
    queryset = Marvel.objects.all()