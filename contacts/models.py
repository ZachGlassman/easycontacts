from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Contact(models.Model):
    EMAIL = 'em'
    PHONE = 'ph'
    IN_PERSON = 'ip'
    OTHER = 'ot'
    CONTACT_TYPE_CHOICES = (
        (EMAIL, 'email'),
        (PHONE, 'phone'),
        (IN_PERSON, 'in person'),
        (OTHER, 'other'),
    )
    
    date = models.DateTimeField('date contacted')
    contact_type = models.CharField(
        max_length =2,
        choices=CONTACT_TYPE_CHOICES,
        default=EMAIL)
        
    def __str__(self):
        return self.date
    