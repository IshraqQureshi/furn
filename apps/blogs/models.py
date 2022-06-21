from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=256)
    publish_date = models.DateField(auto_now=True)
    featured_image = models.FileField(upload_to='blogs')