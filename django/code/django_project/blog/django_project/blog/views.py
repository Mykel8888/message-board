from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Post

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    

class BlogUpadateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

class BlogCreateView(CreateView): #use to edit model object
    model = Post
    template_name ='post_new.html'

    fields = ['title', 'author', 'body']
  
    
    

class BlogViewList(ListView): #itemise object on list
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView): #we use detail view its use display the elements of single object
    model= Post
    template_name = "post_detail.html"

# Create your views here.
