from django.db import models


class Post(models.Model):
    text = models.TextField()
    def __str__(self): #new
        return self.text[: 50] # it will display the first 50 character of the text

