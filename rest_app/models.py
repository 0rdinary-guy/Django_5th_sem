from time import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    #category
    CATEGORY_CHOICES = [
        ('Appetizer', 'Appetizer'),
        ('Main Course', 'Main Course'),
        ('Dessert', 'Dessert'),
        ('Beverage', 'Beverage'),
    ]
    #Fields Starts From Here for the Overall All Menus
    name = models.CharField(max_length=200, help_text="Enter the name of the menu item")
    description = models.TextField(help_text="Enter the Descrption if the menu item", null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Main Course')
    is_available  = models.BooleanField(default=True )

    #Timestamps for better log outputs
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at'] # Orders by latest created first
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['is_available'])
        ]
    def __str__(self):
        return f"{self.name} - ${self.price}"
    
    def get_absolute_url(self):
        return reverse('menu_detail', kwargs={'pk': self.pk})
