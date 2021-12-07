from django.urls import path
from django.urls import path
from demo import views

app_name='demo'  #it is namespace statement

urlpatterns=[
    path('demoa/',views.demoa,name="demoa"),
    path('demob/',views.demob,name="demob"),
    
]