from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    unique_id = models.SlugField(max_length=255, default=uuid.uuid4, unique=True, editable=False,allow_unicode=True)
    name = models.CharField(max_length=300,null=True)
    description = models.TextField(null=True)
    is_publish = models.BooleanField(default=False)
    image = models.ImageField(upload_to='category-backgrounds/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField()


