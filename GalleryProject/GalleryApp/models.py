from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='Images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=100 , default=None)
    # uploaded_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    cat = models.ForeignKey(CategoryModel , on_delete=models.CASCADE)