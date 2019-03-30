from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Article, Author
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_request(request):
    try:
        article = Article.objects.all()
        data = serializers.serialize('json', article)
        return HttpResponse(data)
    except Exception as e:
        HttpResponse(e)


@csrf_exempt
def post_request(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        username = request.POST.get('username')

        post_instace = Article()
        post_instace.title = title
        post_instace.content = content
        post_instace.author = Author.objects.filter(username=username).get()
        post_instace.save()

        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def update_request(request):
    try:
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        username = request.POST.get('username')

        Article.objects.filter(id=id).update(title=title, content=content,
                                             author=Author.objects.filter(username=username).get())

        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def delete_request(request):
    try:
        id = request.POST.get('id')
        Article.objects.filter(id=id).delete()
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(e)
