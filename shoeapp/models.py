from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES=(
    ('MS','Men Shoes'),
    ('WS','Women Shoes'),
    ('BS','Boy Shoes'),
    ('GS','Girl Shoes'),
    ('MSl','Men Slippers'),
    ('WSS','Women Slippers'),
    
)
STATE_CHOICES = {
    ('Haryana','Haryana'),
    ('Delhi','Delhi'),
    ('Jammu','Jammu'),
    ('Rajasthan','Rajasthan'),
    ('Pune','Pune'),
    ('Mumbai','Mumbai'),
    ('Chennai','Chennai'),

}

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=20)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.IntegerField(default=7)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    
)
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)
    

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.IntegerField(default=7)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    



