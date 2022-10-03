from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render
from blog_app1.forms import BlogForm
from blog_app1.models import Blog
# Create your views here.

def base(request):
    return render(request, 'base.html')

# def blog_base(request):
#     return render(request, 'blog_base.html')

def home(request):
    emp = Blog.objects.all()
    return render(request, 'home.html', {'emp':emp})

def add_blog(request):
    if request.method == 'POST':
        var = BlogForm(request.POST)
        if var.is_valid():
            var.save()
            return HttpResponseRedirect('/home/')
    else:
        var = BlogForm()
    return render(request, 'add_blog.html', {'var':var})

def update_blog(request, id):
    if request.method == 'POST':
        sp = Blog.objects.get(pk=id)
        var = BlogForm(request.POST, instance=sp)
        if var.is_valid():
            var.save()
            messages.success(request, "Blog is Updated!!")
            return HttpResponseRedirect('/home/')
            
    else:
        sp = Blog.objects.get(pk = id)
        var = BlogForm(instance=sp)
    return render(request, 'update_blog.html', {'var':var})


def about_blog(request):
    return render(request, 'about_blog.html')


def delete_blog(request, id):
    if request.method == 'POST':
        sp = Blog.objects.get(pk = id)
        sp.delete()
        messages.success(request, "Your Blog has been deleted Successfully!!")
    return HttpResponseRedirect('/home/')