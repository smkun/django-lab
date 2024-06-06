from rest_framework import serializers
from .models import Company
from locations.models import Location
from contacts.models import Contact

class CompanySerializer(serializers.ModelSerializer):
    headquarters = serializers.SerializerMethodField()
    locations = serializers.SerializerMethodField()
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_headquarters(self, obj):
        from locations.serializers import LocationSerializer
        return LocationSerializer(obj.headquarters).data

    def get_locations(self, obj):
        from locations.serializers import LocationSerializer
        return LocationSerializer(obj.locations.all(), many=True).data

    def get_employees(self, obj):
        from contacts.serializers import ContactSerializer
        return ContactSerializer(obj.employees.all(), many=True).data
