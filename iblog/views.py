from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from iblog.models import Post, Category
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
    md = markdown.Markdown(extensions=['markdown.extensions.toc', 'markdown.extensions.codehilite', 'markdown.extensions.extra'])
    post.body = md.convert(post.body)
    post.increase_views()
    return render(request, 'iblog/detail.html', context = { 'post': post, 'form': form, 'comment_list': comment_list, 'toc': md.toc})

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

def category(request, pk):
    cat = get_object_or_404(Category, pk=pk)

    post = cat.post_set.all().order_by('-created_time')

    return render(request, 'iblog/index.html', {'post_list': post})


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    return render(request, 'iblog/index.html', {'post_list':post_list})

def long_profile(request):
    return render(request, 'iblog/full-aboutme.html')
