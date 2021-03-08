from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str(self):
        return self.title
