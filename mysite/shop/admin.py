from django.contrib import admin

# Register your models here.
from .models import User
from .models import Product
from .models import Cart
from .models import CartItem

# Create your views here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
