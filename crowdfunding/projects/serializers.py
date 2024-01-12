from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = '__all__'

class ProjectSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerializer(ProjectSeralizer):
    pledges = PledgeSerializer(many=True, read_only=True)
