from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Publicacao
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
'''
posts_dummy = [{'title': 'This is my first post!',
          'content': 'Hello everybody',
          'author': 'Jack Daniel',
          'date_posted': 'April 06, 2024'},

          {'title': 'Second post coming insane!',
          'content': 'That site will be incredible!',
          'author': 'God2004',
          'date_posted': 'April 08, 2024'},

          {'title': 'Nice webapp, bro',
          'content': 'I really liked the content. Keep improving that, this site has the drip xD',
          'author': 'oppagangnamstyle',
          'date_posted': 'April 10, 2024'},
          ]
'''
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blog(request):
    all_posts = {
        'posts': Publicacao.objects.all()
    }
    return render(request, 'blog/blog.html', all_posts)

class BlogView(ListView):
    model = Publicacao
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserBlogListView(ListView):
    model = Publicacao
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Publicacao.objects.filter(author=user).order_by('-date_posted')

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Publicacao
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class BlogDetailedView(DetailView):
    model = Publicacao

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publicacao
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publicacao
    def get_success_url(self):
        return reverse('site-blog')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
