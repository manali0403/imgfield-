from  django.urls import path
from .views import UserAPI


urlpatterns = [
    path('registr/',UserAPI.as_view())
    
]