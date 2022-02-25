from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('register-nurses/',views.nurses, name='nurses'),
    path('register-assistants/',views.assistants, name='assistants'),
    path('agency-staffs/',views.agency, name='agency'),
    path('recruitment/',views.recruitment, name='recruitment'),
    path('training/',views.training, name='training'),
    path('compliance/',views.compliance, name='compliance'),
    path('registration/',views.registration, name='registration'),
    
]
