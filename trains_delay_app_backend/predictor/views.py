from rest_framework import generics
from .models import Station, Relation
from .api.serializers import StationSerializer, RelationSerializer

class StationView(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class RelationView(generics.RetrieveAPIView):
    queryset = Relation.objects.all()
    serializer_class = RelationSerializer
