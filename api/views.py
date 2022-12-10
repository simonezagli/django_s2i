from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .utils import sendTransaction
import hashlib


def posts(request):
    response = []
    posts = Post.objects.filter().order_by('-datetime')
    for post in posts:
        response.append({
            'datetime': post.datetime,
            'content': post.content,
            'author': f"{post.user.first_name} {post.user.last_name}",
            'hash': post.hash,
            'txId': post.txId
        })
    return JsonResponse(response)


def NewPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.datetime = timezone.now()
            post.writeOnChain()
            #return redirect('posts', {'form': form})
    else:
        form = PostForm()
    return render(request, 'api/new_post.html', {'form': form})




