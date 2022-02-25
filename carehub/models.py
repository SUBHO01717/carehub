
from django.db import models
from django.utils import timezone
# Create your models here.

class Registration(models.Model):
    
    TYPE_CHOICES = (
        ('Nurses', 'Nurses'),
        ('Healthcare Assistants', 'Healthcare Assistants'),
    )
    
    TYPE_CHOICES2 = (
        ('1', 'Qualified nurse with current NMC pin number'),
        ('2', 'Qualified theature nurse with current HPC number'),
        ('3', 'Expeienced Helathcare assitstand'),
    )
    TYPE_CHOICES3 = (
        ('1','Need for work permit,eligible to work in UK'),
        ('2','With work permit,eligible work in UK'),
        ('3', 'In the process of obtaining work permit to work in UK'),
    )
    TYPE_CHOICES4 = (
        ('Un-Responded','Un-Responded'),
        ('Responded','Responded'),
    )
    
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    home_number = models.CharField(max_length=20, blank=True,null=True)
    address= models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    postal_code=models.CharField(max_length=20,blank=True,null=True)
    country=models.CharField(max_length=30)
    profession=models.CharField(choices=TYPE_CHOICES, max_length=255)
    statement = models.CharField(choices=TYPE_CHOICES2, max_length=255)
    experience=models.CharField(max_length=20, blank=True,null=True)
    visa_status=models.CharField(choices=TYPE_CHOICES3, max_length=255)
    upload_CV= models.FileField(upload_to='documents/%Y/%m/%d', blank=True, null=True)
    additional_info=models.TextField(max_length=2000)
    application_date=models.DateField(default = timezone.now)
    status = models.CharField(choices=TYPE_CHOICES4, max_length=255, default="Un-Responded")
    
    def __str__(self):
        return self.first_name + "-" + self.last_name
    
    

class Appointment(models.Model):
    TYPE_CHOICES = (
        ('Agency Staffs', 'Agency Staffs'),
        ('Recruitment', 'Recruitment'),
        ('Training', 'Training'),
    )
    TYPE_CHOICES4 = (
        ('Un-Responded','Un-Responded'),
        ('Responded','Responded'),
    )
    name=models.CharField(max_length=60)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    appointment_on=models.DateField()
    interested_for=models.CharField(choices=TYPE_CHOICES, max_length=255)
    messages=models.TextField()
    application_date=models.DateField(default=timezone.now)
    status = models.CharField(choices=TYPE_CHOICES4, max_length=255, default="Un-Responded")
    
    def __str__(self):
        return self.name + "-" + self.email
    
class Contact(models.Model):
    TYPE_CHOICES= (
        ('Un-Responded','Un-Responded'),
        ('Responded','Responded'),
    )
    name=models.CharField(max_length=255)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    message=models.TextField(blank=True, null=True)
    status=models.CharField(choices=TYPE_CHOICES, max_length=255, default="Un-Responded")
    contact_date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name + "-" + self.email
        