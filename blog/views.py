from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
from blog.forms import UserForm,UserProfileInfoForm, PostForm
from . import forms
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    post_list = Post.objects.order_by('published_date')
    years = []
    tags = []
    categories = []

    for post in post_list :
        year = post.published_date.year
        tag = post.tag
        category = post.category

        if year not in years:
            years.append(year)

        if tag not in tags:
            tags.append(tag)

        if category not in categories:
            categories.append(category)

    paginator = Paginator(post_list, 2) # Show 2 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    my_dict = {'posts':posts, 'years':years, 'tags':tags, 'categories':categories}
    return render(request, 'blog/index.html', context=my_dict)


def post_details(request, pk):
    post_list = Post.objects.get(id=pk)
    my_dict = {'post':post_list}
    return render(request, 'blog/single.html', context=my_dict)

def archeive_posts(request, year):
    post_list = Post.objects.filter(published_date__year = year)
    context = {'year':year,'posts':post_list}
    return render(request, 'blog/archeive.html', context)

def archeive_posts_by_tag(request, tag):
    post_list = Post.objects.filter(tag=tag)
    context = {'posts':post_list}
    return render(request, 'blog/archeive.html', context)

def archeive_posts_by_category(request, category):
    post_list = Post.objects.filter(category=category)
    context = {'posts':post_list}
    return render(request, 'blog/archeive.html', context)

def archeive_posts_by_author(request, author):
    post_list = Post.objects.filter(author=author)
    context = {'posts':post_list}
    return render(request, 'blog/archeive.html', context)

def archeive_posts_by_date(request, year, month, day):
    post_list = Post.objects.filter(published_date__year=year, published_date__month=month, published_date__day=day)
    context = {'posts':post_list}
    return render(request, 'blog/archeive.html', context)

def search_view(request):
        if request.method == 'GET' :
            search_query = request.GET.get('search_box')
            post_list = Post.objects.filter(title__contains=search_query ) | Post.objects.filter(content__contains=search_query ) | Post.objects.filter(tag__contains=search_query ) | Post.objects.filter(category__contains=search_query )
        context = {'posts':post_list}
        return render(request, 'blog/archeive.html', context)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not active")
        else:
            print('Someone tried to login and failed!')
            print('User Name {} and Password {}'.format(username, password))
            return HttpResponse("Invalid login detials provieded")
    else:
        return render(request,'blog/login.html', {})


def registration(request):
    registered = False

    if request.method == 'POST' :
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'blog/sign-up.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered})

@login_required
def post_form_view(request):
    form = forms.PostForm()

    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            print("Form Validation Successful!")
            print("Title:"+ form.cleaned_data['title'])
            print("Content"+ form.cleaned_data['content'])

    return render(request, 'blog/new_post.html',{'form':form})
