from django.urls import path, include
from .views import hello_blog, contact

urlpatterns = [
    path('', hello_blog, name='home'),
    path('contato/', contact, name='contato')
    
]