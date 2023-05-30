from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Blog

# CRUD - Create, Read <= Index, Update, Delete
def index(request):
    blog_posts = Blog.objects.all()
    context = {'blogs': blog_posts}
    return render(request, 'blogs/index.html', context)

def create(request):
    return render(request, 'blogs/create.html')

def get_blog_post(pk):
    try:
        return Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return None

def get_blog_context(blog):
    return {
        'id': blog.id,
        'title': blog.title,
        'contents': blog.contents,
        'author': blog.author,
        'category': blog.category,
        'tags': blog.tags,
        'thumbnail': blog.thumbnail,
        'images': blog.images,
        'updated': blog.updated,
        'created': blog.created,
    }

def update(request, pk):
    blog = get_blog_post(pk)
    if not blog:
        return HttpResponseNotFound("Blog does not exist")
    context = get_blog_context(blog)
    return render(request, 'blogs/update.html', context)

def delete(request, pk):
    blog = get_blog_post(pk)
    if not blog:
        return HttpResponseNotFound("Blog does not exist")
    context = get_blog_context(blog)
    return render(request, 'blogs/delete.html', context)