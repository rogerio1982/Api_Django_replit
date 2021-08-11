

from django.shortcuts import render
from rest_framework import viewsets
from backend.serializers import ProjectSerializer
from backend.serializers import MarvelSerializer
from backend.serializers import IogalSerializer

from backend.models import Project
from backend.models import Marvel
from backend.models import Ioga
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TodoView2(viewsets.ModelViewSet):
    serializer_class = MarvelSerializer
    queryset = Marvel.objects.all()

class TodoView3(viewsets.ModelViewSet):
    serializer_class = IogalSerializer
    queryset = Ioga.objects.all()