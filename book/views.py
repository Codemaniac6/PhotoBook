from django.shortcuts import render


def gallery(request):
    return render(request, 'gallery.html')


def photoDetail(request, pk):
    return render(request, 'photo_detail.html')


def addPhoto(request):
    return render(request, 'add_photo.html')

