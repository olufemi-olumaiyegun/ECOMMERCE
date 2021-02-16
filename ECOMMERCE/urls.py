"""ECOMMERCE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin,auth
from django.urls import path,include
from Items import views as item_view
from users import views as user_views
from . import views as ecommerce_views
from django.contrib.auth import views as authentication_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register,name="register"), #for the registration page
    path('homepage/', ecommerce_views.homepage, name="homepage"),
    path('', ecommerce_views.homepage),
   # path('product',item_view.post,name="uploadproduct"),
    path('accounts/sign-in/', authentication_views.LoginView.as_view(template_name='login.html'),name="signin"), #for sign in page
    #path('accounts/',include('django.contrib.auth.urls'), name='accounts'),
  #  path('logout/', authentication_views.LoginView.as_view(template_name='logout.html'), name="logout"),

]
