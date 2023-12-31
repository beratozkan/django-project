from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    abstract = models.TextField(default='', blank=True)
    pageSize = models.IntegerField(max_length=100, default='', blank=True)
    image = models.ImageField(null=True, blank=True),
    price = models.IntegerField(max_length=100, default='', blank=True)
   
    author_id = models.IntegerField()
    def __str__(self):
        return self.names
   
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(default='', blank=True)
    birht_date = models.DateField(default='', blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
