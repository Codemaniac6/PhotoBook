from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Category, Photo


class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'auth/registration.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('gallery')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistrationView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('gallery')
        return super(RegistrationView, self).get(*args, **kwargs)


class GalleryLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    fields = '__all__'
    success_url = reverse_lazy('gallery')

    def get_success_url(self):
        return reverse_lazy('gallery')


def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'categories': categories, 'photos': photos})


def photoDetail(request, pk):
    photos = Photo.objects.all()
    return render(request, 'photo_detail.html', {'photos': photos})


def addPhoto(request):
    return render(request, 'add.html')

