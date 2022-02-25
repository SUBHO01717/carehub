from cProfile import label
from tkinter.ttk import Style
from django import forms
from . models import *

class RegistrationFrom(forms.ModelForm):
       class Meta:
         model = Registration
         fields = '__all__'
         exclude=('application_date','status')
         labels = {
          
                'first_name':'',
                'last_name':'',
                'email':'',
                'mobile':'',
                'home_number':'',
                'date_of_birth': '',
                'address':'',
                'city':'',
                'postal_code':'',
                'country':'',
                'additional_info':'',
                'experience':'',
        }
        
             
         widgets= {
             'first_name': forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'First Name',}),
             'last_name': forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder': 'Last Name',}),
             'email': forms.EmailInput(attrs={'class':'form-control mb-2','placeholder': 'Email',}),
             'mobile': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Mobile Number',}),
             'home_number': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Home Number (Optional)',}),
             'date_of_birth': forms.DateInput(attrs={'class':'form-control mb-2', 'type':'date',}),
             'address': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Address',}),
             'city': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'City',}),
             'postal_code': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Postal Code',}),
             'country': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Country',}),
             'experience': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Years/Months of Experience',}),
             'visa_status': forms.Select(attrs={'class':'form-control mb-2',}),
             'profession': forms.Select(attrs={'class':'form-control mb-2',}),
             'statement': forms.Select(attrs={'class':'form-control mb-2',}),
             'upload_CV': forms.FileInput(attrs={'class':'form-control mb-2',}),
             'additional_info': forms.Textarea(attrs={'class':'form-control mb-2', 'placeholder': 'Your Messages (if any)',}),
        }

class AppointmentForm(forms.ModelForm):
       class Meta:
         model = Appointment
         fields = '__all__'
         exclude=('application_date','status')
         labels = {
          
                'name':'',
                'email':'',
                'phone':'',
                'appointment_on':'',
                'messages': '',
        }
        
             
         widgets= {
             'name': forms.TextInput(attrs={'class':'form-control mb-2 col-md-6', 'placeholder': 'First Name',}),
             'email': forms.EmailInput(attrs={'class':'form-control mb-2','placeholder': 'Email',}),
             'phone': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Mobile Number',}),
             'appointment_on': forms.DateInput(attrs={'class':'form-control mb-2', 'type':'date'}),
             'interested_for': forms.Select(attrs={'class':'form-control mb-2',}),
             'messages': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Your Messages (if any)',}),
        }


class ContactForm(forms.ModelForm):
       class Meta:
         model = Contact
         fields = '__all__'
         exclude=('status','contact_date')
         labels = {
          
                'name':'',
                'email':'',
                'subject':'',
                'message':'',
        }             
         widgets= {
             'name': forms.TextInput(attrs={'class':'form-control mb-2 col-md-6', 'placeholder': 'First Name',}),
             'email': forms.EmailInput(attrs={'class':'form-control mb-2 col-md-6','placeholder': 'Email',}),
             'subject': forms.TextInput(attrs={'class':'form-control mb-2','placeholder': 'Subject',}),
             'message': forms.Textarea(attrs={'rows':5,'class':'form-control mb-2','placeholder': 'Your Message',}),
        }
