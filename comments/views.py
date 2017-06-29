from django.shortcuts import render, get_object_or_404, redirect
from iblog.models import Post
from comments.models import Comment
from comments.form import CommentForm


# Create your views here.

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    # check the method
    if request.method == 'POST':
        print('receive the post')
        # construct the instance of comment form
        form = CommentForm(request.POST)

        # check if the data in the form is correct in format
        if form.is_valid():
            print('valid')
            comment = form.save(commit=False) # generate the comment from the comment form
            comment.post = post # relate to the post
            comment.save() # save to comment database

            return redirect(post) # redirect to post.get_absolute_url
        else:
            # find invalid, return to error page
            comment_list = post.comment_set.all()
            context = {'post': post, 'form': form, 'comment_list': comment_list}
            return render(request, 'iblog/detail.html', context=context)
    else:
        return redirect(post)
