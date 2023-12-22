from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    

    def __str__(self):
        return self.name


class Unit(models.Model):
    PROPERTY_TYPES = (
        ('1BHK', '1 Bedroom, Hall, Kitchen'),
        ('2BHK', '2 Bedroom, Hall, Kitchen'),
        ('3BHK', '3 Bedroom, Hall, Kitchen'),
        ('4BHK', '4 Bedroom, Hall, Kitchen'),
    )

    property = models.ForeignKey(Property, related_name='units', on_delete=models.CASCADE)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=4, choices=PROPERTY_TYPES)
    

    def __str__(self):
        return f"{self.type} - Property: {self.property.name}"


class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    document_proofs = models.TextField()
    unit = models.ForeignKey(Unit, related_name='tenants', on_delete=models.CASCADE)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.IntegerField()
    

    def __str__(self):
        return self.name
