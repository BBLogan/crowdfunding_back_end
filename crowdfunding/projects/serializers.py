from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Pledge
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Project
        fields = '__all__'

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    total_amount_received = serializers.SerializerMethodField()

    def get_total_amount_received(self, obj):
        return obj.total_amount_received()

    def update(self, instance, validated_data):
        #call the update method of the parent class to preserve default behaviour
        instance = super().update(instance, validated_data)
        #my custom logic to update addtional fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        #save the instance
        instance.save()
        #return the updated instance
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.supporter = validated_data.get('supported_pledges', instance.supporter)
        instance.save()
        return instance