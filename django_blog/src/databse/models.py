from django.db import models

# Create your models here.

class BlogPost(models.Model):
    img = models.ImageField(upload_to="gallery/", height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=26)
    content = models.TextField()
