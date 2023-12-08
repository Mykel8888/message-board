from django.db import models

# Create your models here.

from django.urls import reverse

class Post(models.Model):
    title=models.CharField(max_length=200)
    author =models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()

    def __str__(self):
        return self.title #display the data title in admin page
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    #this is where our editing will be land
