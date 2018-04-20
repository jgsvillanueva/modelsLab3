"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from shop import views

urlpatterns = [
    url(r'^product/$', views.ProductList.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
    url(r'^user/$', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^cart/$', views.CartList.as_view()),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),
    url(r'^cart_item/$', views.CartItemList.as_view()),
    url(r'^cart_item/(?P<pk>[0-9]+)/$', views.CartItemDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
