from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, FormView
from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    categories = Category.objects.all()
    return render(request, 'gallery.html', {'categories': categories, 'photos': photos})


class GalleryView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = context['photos'].filter(user=self.request.user)
        context['categories'] = Category.objects.all()

        return context


def photoDetail(request, pk):
    if request.user.is_anonymous:
        redirect(reverse_lazy('login'))
    picture = Photo.objects.get(id=pk)
    category = picture.category
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo_detail.html', {'photos': photos, 'photo': photo})


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'add.html'
    fields = ['title', 'description', 'category', 'image']
    success_url = reverse_lazy('gallery')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        if self.request.method == 'POST':
            data = self.request.POST
            image = self.request.FILES.get('image')

            if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])
            elif data['new_category'] != '':
                category, created = Category.objects.get_or_create(name=data['category_new'])
            else:
                category = None

            photo = Photo.objects.create(
                user=self.request.user,
                category=category,
                description=data['description'],
                title=data['title'],
                image=image
            )
        return super(AddPhotoView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photo_detail.html'
    success_url = reverse_lazy('gallery')


class CategoryDeleteView(DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'photo_detail.html'
    success_url = reverse_lazy('gallery')