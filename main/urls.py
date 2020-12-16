from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('add-patient',views.addPatient,name='add-patient'),
    path('update-patient/<int:id>',views.updatePatient,name='update-patient'),
    path('delete-patient/<int:id>',views.deletePatient,name='delete-patient'),
    path('send-email/<int:id>',views.sendEmail,name='send-email'),
]