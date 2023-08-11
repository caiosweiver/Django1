from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import Format

class post_list(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ['-created_at']

class post_ref(DetailView):
    model = Post
    template_name = 'post_ref.html'

class my_posts(ListView):
    model = Post
    template_name = 'my_posts.html'
    ordering = ['-created_at']

class create_posts(CreateView):
    model = Post
    template_name = 'create_posts.html'
    form_class = Format

class edit_posts(UpdateView):
    model = Post
    template_name = 'edit_posts.html'
    form_class = Format

class delete_posts(DeleteView):
    model = Post
    template_name = 'delete_posts.html'
    success_url = reverse_lazy('post_list')

def homepage(request):
    return render(request, 'homepage.html')

def about_page(request):
    return render(request, 'about_page.html')