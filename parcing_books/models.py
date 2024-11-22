
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=900)
    image = models.ImageField(upload_to='books/')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00,null=True)
    rating = models.CharField(max_length=10)




    def __str__(self):
        return self.title
