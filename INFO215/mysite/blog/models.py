from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title

"""
title and content are attributes where we can store strings. The __str__ method
just tells Django what to print when it needs to print out an instance of the
Post model.
"""