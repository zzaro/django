from django.db import models
from django.urls import reverse


# Create your models here.
class Members(models.Model):
    name = models.CharField('NAME', max_length=100, blank=False)
    age = models.CharField('AGE', max_length=100, blank=True)
    address = models.CharField('ADDRESS', max_length=200, blank=False)
    tel = models.CharField('TEL', max_length=100, blank=False)
    email = models.EmailField('EMAIL', max_length=100, blank=False)
    birth = models.DateTimeField('BIRTH', auto_now=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('members_detail', args=(self.name,))