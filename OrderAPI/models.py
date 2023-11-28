from django.db import models

class Place(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.slug
    

#create models here
class Logger(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    order_time = models.DateField(auto_now=True)
    age = models.IntegerField()
    place = models.ForeignKey(Place, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name