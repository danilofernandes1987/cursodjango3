from django.shortcuts import render
from .models import Post


def hello_blog(request):
   
    return render( request, 'index.html')

def contact(request):
    return render( request, 'contact.html')