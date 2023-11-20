from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


# Create your views here.
class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'postView'

class PostList(ListView):
    # Model to output
    model = Post
    # template for output
    template_name = 'news_list.html'
    # list name
    context_object_name = 'postList'
    queryset = Post.objects.order_by('-created_at')
