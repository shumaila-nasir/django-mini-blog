from django.shortcuts import render, redirect
from .forms import SignupForm , LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth import login as login_auth
from .models import Post
from django.contrib.auth.models import Group


# home
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# about
def about(request):
    return render(request, 'blog/about.html')

# contact
def contact(request):
    return render(request, 'blog/contact.html')

# dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': full_name,
                                                       'groups':gps})
    else:
        return redirect('/login/')

# signup
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.errors)
        if form.is_valid():
            messages.success(request, 'You are registered here')

            print("save 1")
            user = form.save()
            print('save')
            group = Group.objects.get(name='Author Group')
            user.groups.add(group)
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form':form})

def login(request):
    # import pdb
    # pdb.set_trace()
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data=request.POST)
            print('login')
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login_auth(request, user)
                    messages.success(request, 'login Succeccfully!!')
                    return redirect('/dashboard/')

        else:
            form = LoginForm()
            print("not login")
        return render(request, 'blog/login.html', {'form': form})
    else:
        return redirect('/dashboard/')

def user_logout(request):
    logout(request)
    return redirect('/')

def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                pst = Post(title=title, description=description)
                pst.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    else:
        return redirect('/login/')

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi= Post.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            print(form)
            if form.is_valid():
                form.save()
                print(form)
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/update.html', {'form':form})
    else:
        return redirect('/login/')

def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return redirect("/dashboard/")
        else:
            return redirect('/login/')