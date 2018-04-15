from django.db import models

class time_stamp(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class User(models.Model):
    u_email = models.EmailField(max_length = 254)
    u_fname = models.CharField(max_length = 200)
    u_lname = models.CharField(max_length = 200)

class Product(models.Model):
    prod_name = models.CharField(max_length = 200)
    prod_price = models.DecimalField(max_digits=18, decimal_places=2)
    prod_description = models.CharField(max_length = 200)

class Cart(time_stamp):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_code = models.CharField(max_length = 30)
    cart_paid = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(max_digits=18, decimal_places=2, default=0.00)
