from rest_framework import serializers
from ..models import Station, Relation

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['relation_name'] = instance.relation_name.split('_')[0]
        return representation