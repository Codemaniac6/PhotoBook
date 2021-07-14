from django.urls import path
from . import views


urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('photo/<str:id>', views.photoDetail, name='photo_detail'),
    path('add/', views.addPhoto, name='addPhoto'),
]