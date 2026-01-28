from django.db import models

# Create your models here.
class Menu(models.Model):
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Image = models.ImageField()
    
    def __str__(self):
        return self.Name