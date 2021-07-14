from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('', gallery, name='gallery'),
    path('photo/<str:pk>', photoDetail, name='photo_detail'),
    path('add/', addPhoto, name='add'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', GalleryLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]