
from django.urls import path
from sample import views

app_name='sample'  #it is namespace statement

urlpatterns=[
    path('demoa/',views.demoa,name="demoa"),
    path('demob/',views.demob,name="demob"),
    
]