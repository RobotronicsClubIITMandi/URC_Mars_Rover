from distutils.command.upload import upload
from django.db import models
import re

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='blogs/')
    text = models.CharField(max_length=10000)

    def short_text(self):
        text_len = min(300, len(self.text))
        return self.text[:text_len]

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)