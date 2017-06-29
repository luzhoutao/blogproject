from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from iblog.models import Post
import markdown
from comments.form import CommentForm
# Create your views here

def index(request):
    post_list = Post.objects.all()
    return render(request, 'iblog/index.html', context = {'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    form = CommentForm()
    comment_list = post.comment_set.all()
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.toc', 'markdown.extensions.codehilite', 'markdown.extensions.extra'])
    return render(request, 'iblog/detail.html', context = { 'post': post, 'form': form, 'comment_list': comment_list})

def aboutme(request):
    return render(request, 'iblog/about.html')

def contact(request):
    return render(request, 'iblog/contact.html')

# placeholder for trying haystack
def search(request):
    q = request.GET.get('q')
    err_msg = ''

    if not q:
        err_msg = 'Please enter the keyword.'
        return render(request, 'iblog/result.html', {'err_msg': err_msg})

    post_list = Post.objects.filter(title__icontains=q)
    return render(request, 'iblog/result.html', {'err_msg': err_msg, 'post_list':post_list})
