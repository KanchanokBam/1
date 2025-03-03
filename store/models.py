from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('member', 'Member'),
        ('store', 'Store'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')

# Product Model
class Product(models.Model):
    store = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ ลบ limit_choices_to
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'กำลังเตรียมสินค้า'),
        ('ready', 'พร้อมรับสินค้า'),
        ('completed', 'สำเร็จ'),
    ]
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"
