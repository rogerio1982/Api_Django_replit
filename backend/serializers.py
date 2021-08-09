from rest_framework import serializers
from .models import Project
from .models import Marvel


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology','image')

class MarvelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology','image')