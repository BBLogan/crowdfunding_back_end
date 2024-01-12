from rest_framework import serializers
from .models import Projects, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = '__all__'

class ProjectSeralizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Projects
        fields = '__all__'

class ProjectDetailSerializer(ProjectSeralizer):
    pledges = PledgeSerializer(many=True, read_only=True)