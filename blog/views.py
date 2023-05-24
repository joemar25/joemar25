from django.http import HttpResponseNotFound
from django.shortcuts import render

# mar - sample contents before implementing the databse for blogs (we need a good relational simple databse)
blog_posts = [
    {'id':'1', 'title':'My First Blog Post', 'contents':'This is my first blog post. Welcome to my blog!', 'author':'John Doe', 'date':'2021-09-01', 'category':'Introduction', 'tags':['blogging', 'introduction'], 'images':{'1.jpg', '2.jpg'}},
    {'id':'2', 'title':'My Favorite Python Libraries', 'contents':'In this blog post, I will share my favorite Python libraries and how I use them in my projects.', 'author':'John Doe', 'date':'2021-09-05', 'category':'Python', 'tags':['python', 'libraries'], 'images':{'3.jpg', '4.jpg'}},
    {'id':'3', 'title':'How to Stay Motivated as a Developer', 'contents':'In this blog post, I will share my tips on how to stay motivated as a developer and avoid burnout.', 'author':'John Doe', 'date':'2021-09-10', 'category':'Motivation', 'tags':['motivation', 'developer'], 'images':{'5.jpg', '6.jpg'}},
    {'id':'4', 'title':'My Experience with Remote Work', 'contents':'In this blog post, I will share my experience with remote work and how I stay productive while working from home.', 'author':'John Doe', 'date':'2021-09-15', 'category':'Remote Work', 'tags':['remote work', 'productivity'], 'images':{'7.jpg', '8.jpg'}}
]

# CRUD - Create, Read <= Index, Update, Delete
def index(request):
    context = {'blogs': blog_posts}
    return render(request, 'blog/index.html', context)

def create(request):
    return render(request, 'blog/create.html')

def get_blog_post(pk):
    try:
        return blog_posts[int(pk)-1]
    except IndexError:
        return None

def get_blog_context(blog):
    return {
        'id': blog['id'],
        'title': blog['title'],
        'contents': blog['contents'],
        'author': blog['author'],
        'date': blog['date'],
        'category': blog['category'],
        'tags': blog['tags'],
        'images': blog['images'], 
    }

def update(request, pk):
    blog = get_blog_post(pk)
    if not blog:
        return HttpResponseNotFound("Blog does not exist")
    context = get_blog_context(blog)
    return render(request, 'blog/update.html', context)

def delete(request, pk):
    blog = get_blog_post(pk)
    if not blog:
        return HttpResponseNotFound("Blog does not exist")
    context = get_blog_context(blog)
    return render(request, 'blog/delete.html', context)