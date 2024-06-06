from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    home = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    employers = serializers.SerializerMethodField()

    class Meta:
        model = Contact
        fields = '__all__'

    def get_home(self, obj):
        from locations.serializers import LocationSerializer
        return LocationSerializer(obj.home).data

    def get_locations(self, obj):
        from locations.serializers import LocationSerializer
        return LocationSerializer(obj.locations.all(), many=True).data

    def get_employers(self, obj):
        from companies.serializers import CompanySerializer
        return CompanySerializer(obj.companies.all(), many=True).data
