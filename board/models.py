from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_in = models.DateTimeField(auto_now_add=True)
    content = HTMLField(verbose_name=_("Content"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))


class Response(models.Model):
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='responses')
    content = models.TextField(verbose_name=_("Content"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    date_in = models.DateTimeField(auto_now_add=True)


