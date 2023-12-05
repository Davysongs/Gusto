from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    description = models.TextField()
    def __str__(self):
        return self.name + ' - $' + str(self.price)
        