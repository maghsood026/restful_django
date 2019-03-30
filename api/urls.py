from . import views
from django.urls import path

urlpatterns = [
    path('get/', views.get_request, name='get_article'),
    path('insert/', views.post_request, name='insert_article'),
    path('update/', views.update_request, name='update_article'),
    path('delete/', views.delete_request, name='delete_article'),
]
