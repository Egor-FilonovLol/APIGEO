from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Location, Message


class LocationSerializers(ModelSerializer):

    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    lon = serializers.ReadOnlyField(source='point.x')
    lat = serializers.ReadOnlyField(source='point.y')

    class Meta:
        model = Location
        fields = ('id', 'name', 'lat', 'lon', 'description', 'latitude',
                  'longitude')

    def validate_latitude(self, value):
        if not (value >= -90 and value <= 90):
            raise serializers.ValidationError('Введите широту от -90 до 90 '
                  '(включително)')
        return value

    def validate_longitude(self, value):
        if not (value >= -180 and value <= 180):
            raise serializers.ValidationError('Введите долготу от -180 до 180(включительно)')
        return value


class HelpSerializer(ModelSerializer):
    lon = serializers.ReadOnlyField(source='point.x')
    lat = serializers.ReadOnlyField(source='point.y')

    class Meta:
        model = Location
        fields = ('id', 'name', 'lat', 'lon',)


class MessageSerializer(ModelSerializer):
    location = HelpSerializer(read_only=True)
    author = serializers.CharField(read_only=True, source='author.username')

    class Meta:
        model = Message
        fields = ('id', 'message', 'location', 'author',)
