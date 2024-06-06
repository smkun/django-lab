from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    companies = models.ManyToManyField('companies.Company', related_name='company_locations', blank=True)
    inhabitants = models.ManyToManyField('contacts.Contact', related_name='location_inhabitants', blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}"
