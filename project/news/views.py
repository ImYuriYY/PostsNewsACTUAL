from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'news'



class AuthorView(DetailView):
    model = Author
    template_name = 'author_info.html'
    context_object_name = 'author'



class CreatePostView(CreateView):
    model = Post
    form_class = NewPostForm
    template_name = 'create.html'
    success_url = '/news/'



class EditPostView(UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'edit.html'
    success_url = '/news/'




class DeletePostView(DeleteView):
    model = Post
    success_url = '/news/'
    template_name = 'confirm_delete_post.html'

