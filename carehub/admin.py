from csv import list_dialects
from django.contrib import admin
from . models import *
# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    list_display =('first_name','last_name','email','mobile', 'country','profession','application_date','status','upload_CV')

admin.site.register(Registration, RegistrationAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display =('name','email','phone','appointment_on','interested_for','application_date','status')

admin.site.register(Appointment, AppointmentAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display =('name','email','subject','contact_date','status')

admin.site.register(Contact, ContactAdmin)