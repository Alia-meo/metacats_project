from django.shortcuts import render, get_object_or_404
from requests import post

from users.forms import CommentForm
from .models import Post
from maincat.views import menu
from django.views.generic.edit import FormMixin
from .models import *
from .forms import CommentForm


def blog_all(request):
    post = Post.objects.all()
    return render(request, 'blog/blog_all.html', {'posts': post, 'menu': menu,})


def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = CommentPost.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.user = request.user
            comm.post = post
            comm.save()
        else:
            form = CommentForm()
    return render(request, 'blog/blog_single.html', {'post': post, 'menu': menu,
                                                     'form': form, 'comment': comment})

# def blog(request):
#     posts = Articles.objects.get(pk=1 )
#     form = CommentForm(request.POST)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comm = form.save(commit=False, Null=True)
#             comm.author = request.author
#             # comm.article_comment = posts
#             comm.save()
#         else:
#             form = CommentForm()
#     return render(request, 'blog/blog_single.html', {'posts': posts, 'menu': menu, 'form': form})
# class HomeDetailView(FormMixin):
#     form_class = CommentForm


