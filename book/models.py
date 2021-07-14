from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    photo = models.ImageField(blank=False, null=False)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
