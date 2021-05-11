from django.db import models


# Create your models here.


class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=10000)
    blog_text = models.TextField(max_length=10000)

    def __str__(self):
        return self.title