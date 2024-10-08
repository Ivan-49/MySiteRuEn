from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
# from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def article_detail(request, slug):
    instance = get_object_or_404(Article, slug=slug)
    global head 
    head = Article.objects.all()

    for i in head:
        print(i.url)

    if request.path in '/en/home/':
        img = True
    else:
        img = False

    context = {
        'instance':instance,
        'head':head,
        'img':img
    }
    
    print(f'instance url = {instance.url}')
    print(f'main/{instance.url}.html')
    try:
        return render(request, f'main/{instance.url}.html', context)
    except:
        return render(request, 'main/home.html', context)


def redirect_home(request):
    return redirect('/home/')