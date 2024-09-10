from django.db import models
class Website(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2500)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    COFFEE_CHOICES = [
        ('Espresso', 'Espresso'),
        ('Latte', 'Latte'),
        ('Cappuccino', 'Cappuccino'),
        ('Mocha', 'Mocha'),
    ]
    
    coffee = models.CharField(max_length=20, choices=COFFEE_CHOICES, default='Espresso')
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    coffee_type = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.quantity} x {self.coffee})"