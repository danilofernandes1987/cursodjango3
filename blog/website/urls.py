from django.urls import path, include
from .views import hello_blog, contact
from .views import post_detail

urlpatterns = [
    path('', hello_blog, name='home'),
    path('contato/', contact, name='contato'),
    path('post/<int:id>/', post_detail, name='post_detail')
    
]