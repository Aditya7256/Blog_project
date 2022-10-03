from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from blog_app1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('blog_app1.urls')),
    path('', views.base, name = 'base'),
    
]
