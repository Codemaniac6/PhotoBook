from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('', GalleryView.as_view(), name='gallery_view'),
    path('', gallery, name='gallery'),
    path('photo/<str:pk>', photoDetail, name='photo_detail'),
    path('add/', AddPhotoView.as_view(), name='add'),
    path('delete/<str:pk>', PhotoDeleteView.as_view(), name='photo_delete'),
    path('delete/<str:id>', CategoryDeleteView.as_view(), name='category_delete'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('login/', GalleryLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]