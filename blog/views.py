from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def starting_page(request):
    latest_posts = Project.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    list_posts = Project.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html",{
        "all_posts": list_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Project, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })