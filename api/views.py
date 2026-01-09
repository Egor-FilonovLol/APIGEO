from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.geos import Point
from .models import Location, Message
from .serializers import LocationSerializers, MessageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


class LocationCreateView(CreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        lat = serializer.validated_data.pop('latitude')
        lon = serializer.validated_data.pop('longitude')
        point = Point(lon, lat)
        serializer.save(author=self.request.user, point=point)


class MessageLocationView(CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        location = get_object_or_404(Location, id=self.kwargs['location_id'])
        serializer.save(author=self.request.user, location=location)


class SearchPoint(ListAPIView):
    serializer_class = LocationSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        lat = self.request.query_params.get('latitude')
        lon = self.request.query_params.get('longitude')
        radius = self.request.query_params.get('radius')

        if lat is None or lon is None:
            raise ValidationError('не может быть 0')
        if radius is None:
            raise ValidationError('вам нужно указать радиус')
        lat = float(lat)
        lon = float(lon)
        radius = float(radius)*1000
        point = Point(lon, lat)
        return Location.objects.filter(
                point__dwithin=(point, radius)
        )


class MessageRadius(ListAPIView):

    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        lat = self.request.query_params.get('latitude')
        lon = self.request.query_params.get('longitude')
        radius = self.request.query_params.get('radius')

        if lat is None or lon is None:
            raise ValidationError('не может быть 0')
        if radius is None:
            raise ValidationError('вам нужно указать радиус')
        try:
            lat = float(lat)
            lon = float(lon)
            radius = float(radius)*1000
            point = Point(lon, lat)
        except TypeError:
            raise ValidationError('Не удалось сделать float, непрравильно введено')
        return Message.objects.filter(
                location__point__dwithin=(point, radius)
        )
