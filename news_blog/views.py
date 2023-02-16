from django.shortcuts import render, redirect
from .models import Post, UserSignUpForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'news_blog/index.html', context)


def login(request):
    return render(request, 'news_blog/login.html', {'title': "Login Page"})


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account Successfully Created for {username} Login Now!')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'news_blog/sign_up.html', {
        'form': form,
        'title': "Signup Page"
        })


def article_view(request):
    return render(
        request, 'news_blog/article_view.html', {'title': "Article View"})


def post_creation(request):
    return render(
        request, 'news_blog/post_creation.html', {'title': "Post Creation"})


def view_all(request):
    return render(request, 'news_blog/view_all.html', {'title': "All Posts"})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

# u_form = UserUpdateForm()
# p_form = ProfileUpdateForm()
    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'news_blog/profile.html', context)
