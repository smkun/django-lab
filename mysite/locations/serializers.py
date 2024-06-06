from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    inhabitants = serializers.SerializerMethodField()
    companies = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = '__all__'

    def get_inhabitants(self, obj):
        from contacts.serializers import ContactSerializer
        return ContactSerializer(obj.inhabitants.all(), many=True).data

    def get_companies(self, obj):
        from companies.serializers import CompanySerializer
        return CompanySerializer(obj.companies.all(), many=True).data
