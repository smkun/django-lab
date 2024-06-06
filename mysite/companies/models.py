from django.db import models
from locations.models import Location
from contacts.models import Contact

class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    headquarters = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='company_headquarters', null=True, blank=True)
    locations = models.ManyToManyField(Location, related_name='associated_companies', blank=True)
    employees = models.ManyToManyField(Contact, related_name='employing_companies', blank=True)

    def __str__(self):
        return self.name
