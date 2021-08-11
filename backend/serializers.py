from rest_framework import serializers
from .models import Project
from .models import Marvel
from .models import Ioga

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology','image')

class MarvelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology','image')

class IogalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology','image')