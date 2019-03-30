from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Article
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_request(request):
    article = Article.objects.all()
    data = serializers.serialize('json', article)
    return HttpResponse(data)


@csrf_exempt
def post_request(request):
    pass


@csrf_exempt
def update_request(request):
    pass


@csrf_exempt
def delete_request(request):
    pass
