import requests
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template.loader import get_template
from databse.models import BlogPost

def home_page(request):
    qs = BlogPost.objects.all().order_by("-pk")[:3]
    blog_posts = []
    for each in qs:
        blog_posts.append(each)

    context = {
        'posts' : blog_posts,
        'title' : "Chronicles of Ezzypoo"
    }
    return render(request, "base.html", context)

def posts_page(request):
    qs = BlogPost.objects.all().order_by("-pk")
    blog_posts = []
    for each in qs:
        blog_posts.append(each)

    context = {
        'posts' : blog_posts,
        'title' : "All Posts"
    }
    return render(request, "all_posts.html", context)

def post_view(request, id):
    qs = BlogPost.objects.get(id=id)
    context = {
        'post' : qs,
        'title' : qs.title
    }
    return render(request, "detail_view.html", context)
