from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment
from . import forms
# Create your views here.

def index(request):
    post_list = Post.objects.order_by('published_date')
    my_dict = {'posts':post_list}
    return render(request, 'blog/index.html', context=my_dict)

def post_form_view(request):
    form = forms.PostForm()

    if request.method == 'POST':
        form = forms.PostForm(request.POST)

        if form.is_valid():
            print("Form Validation Successful!")
            print("Title:"+ form.cleaned_data['title'])
            print("Content"+ form.cleaned_data['content'])

    return render(request, 'blog/new_post.html',{'form':form})
