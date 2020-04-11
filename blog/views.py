from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, PostSubscriber,Comment


def index(request):
    post = Post.published.all()

    # Adding Paginator Functionality.
    paginator = Paginator(post, 4)  # 1 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    if request.method == "POST":
        name = request.POST["Name"]
        email=request.POST["Email"]
        subscriber = PostSubscriber(name=name, email=email)
        subscriber.save()
        return HttpResponseRedirect('/')

    context = {'post': post, 'page': page, 'posts': posts}
    return render(request, 'blog/index.html', context)


def post(request, slug):
    posts = Post.published.all()
    post = get_object_or_404(Post, slug=slug)
    comment = post.comments.all()
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        new_comment = Comment(name=name, email=email,
                              message=message, post=post)
        new_comment.save()
        return HttpResponseRedirect('/')
    
    context = {'post': post, 'posts': posts,'comment':comment}
    return render(request, 'blog/post.html', context)

