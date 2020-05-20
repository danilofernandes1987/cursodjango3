from django.shortcuts import render
from .models import Post


def hello_blog(request):
   
    lista_posts = Post.objects.all()
    data = {'posts': lista_posts}
    return render( request, 'index.html', data)

def contact(request):
    return render( request, 'contact.html')

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})