from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POSTS_ON_PAGE = 10


def index(request):
    title = 'Это главная страница прокта Yatube'
    text = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:POSTS_ON_PAGE]
    context = {
        'posts': posts,
        'title': title,
        'text': text,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = 'Здесь будет информация о группах проекта Yatube'
    group = get_object_or_404(Group, slug=slug)
    posts = (
            Post.objects.filter(group=group).order_by('-pub_date')
            [:POSTS_ON_PAGE]
    )
    context = {
        'group': group,
        'posts': posts,
        'title': title,
        'slug': slug,
    }
    return render(request, 'posts/group_list.html', context)
