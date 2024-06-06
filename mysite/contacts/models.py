from django.db import models
from locations.models import Location

class Contact(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    home = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='contact_home', null=True, blank=True)
    locations = models.ManyToManyField(Location, related_name='contact_locations', blank=True)
    companies = models.ManyToManyField('companies.Company', related_name='company_employees', blank=True)

    def __str__(self):
        return self.name
