"""
URL configuration for shop project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from product.views import hello_view, current_date_view, goodby_view, product_list_view, main_page_view,\
    product_detail_view, category_list_view, product_create_view

from user.views import registration_view, login_view, profile_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_page_view, name="main_page"),
    path('hello/', hello_view, name='hello'),
    path('current_date/', current_date_view, name='current_date'),
    path('goodby/', goodby_view, name='goodby'),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:product_id>/', product_detail_view, name='product_detail'),
    path('categories/', category_list_view, name='category_list'),
    path('create/', product_create_view, name='product_create'),

    path('registration/', registration_view, name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('profile/', profile_view, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
