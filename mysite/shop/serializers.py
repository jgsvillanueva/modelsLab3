from rest_framework import serializers
from shop.models import Product, Cart, CartItem, User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('prod_name', 'prod_price', 'prod_description')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('u_email', 'u_fname', 'u_lname')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'cart_code', 'cart_paid', 'total_price')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('cart', 'product', 'quantity', 'line_total')
