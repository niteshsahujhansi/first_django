from django.urls import URLPattern, path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),       # inside views file home function called 
    path('add', views.add, name='add')       # inside views file add function called 
]
