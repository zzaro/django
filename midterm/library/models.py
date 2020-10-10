from django.db import models


# Create your models here.
class Library(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=False)
    author = models.CharField('AUTHOR', max_length=50, blank=False)
    publisher = models.CharField('PUBLISHER', max_length=50, blank=False)
    category = models.CharField('CATEGORY', max_length=50, blank=True)
    isbn_code = models.CharField('ISBN_CODE', max_length=100, unique=True)

    def __str__(self):
        return self.title
