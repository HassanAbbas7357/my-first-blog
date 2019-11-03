from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from .models import Category,Post,Comment,Contact,Manage_Blog_Images,About
from .forms import Comment_form,Contact_form

def home(request):
    #p = get_object_or_404(Post)
    categories = Category.objects.all()
    posts = Post.objects.all().order_by("-post_published_date")
    manage = get_object_or_404(Manage_Blog_Images)

    return render(request,'home.html',{'categories':categories,
                                        'posts':posts,
                                        'manage':manage})
                                        #'p':p})

def sug(request):
    manage = get_object_or_404(Manage_Blog_Images)
    return render(request,'sug.html',{'manage':manage})



def contact(request):
    categories = Category.objects.all()
    form = Contact_form(request.POST or None)
    if form.is_valid():
        contact = Contact(
            name = form.cleaned_data["name"],
            email = form.cleaned_data["email"],
            message = form.cleaned_data["message"]
            )
        contact.save()
        return home(request)
    
    #form = Contact_form()
    return render(request,'contact.html',{'form':form,'categories':categories})

def cat(request,slug):
    cats = get_object_or_404(Category,slug=slug)
    posts = Post.objects.filter(category=cats)
    manage = get_object_or_404(Manage_Blog_Images)
    categories = Category.objects.all()
    return render(request,'cat.html',{'cats':cats,'posts':posts,'manage':manage,'categories':categories})

def detail(request,slug):
    categories = Category.objects.all()
    posts = get_object_or_404(Post,slug=slug)
    manage = get_object_or_404(Manage_Blog_Images)
    comments = Comment.objects.filter(post=posts)
    form = Comment_form(request.POST or None)
    if form.is_valid():
        comment = Comment(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                comment_text=form.cleaned_data["comment_text"],
                post=posts,
            )
        comment.save()
        form = Comment_form()
        return HttpResponseRedirect(request.path_info)
    #form = Comment_form(request.POST or None)

    return render(request,'detail.html',{'manage':manage,'categories':categories,'posts':posts,'comments':comments,'form':form})

@login_required
def delete(request,slug):
    posts = get_object_or_404(Post,slug=slug)
    if request.method == 'POST':
        posts.delete()
        return home(request)
     
    template_name = 'delete.html'
    return render(request,template_name,{'posts':posts})

def login_user_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        #if user exists
        if user:
            if user.is_active:
                login(request,user)
                return home(request)
            else:
                HttpResponse("ACCOUNT NOT ACTIVE")
        
        else:
            
            return HttpResponse("User Does not exists or invalid login details")
            
    else:
        return render(request,'login.html')
    return render(request,'login.html')


@login_required
def logout_user(request):
    logout(request)
    return home(request)

def about(request):
    ab = get_object_or_404(About)
    return render(request,'about.html',{'cat':ab})