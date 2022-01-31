from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    text = models.CharField(max_length=10000)

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)