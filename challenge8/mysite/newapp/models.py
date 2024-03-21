from django.db import models


# Create your models here.

class Book(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    image = models.CharField(max_length=500, default="https://clipartix.com/wp-content/uploads/2019/03/stack-of-books-clipart-18-2019-22.jpg")
    rating = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='fiction')
