from django.contrib import admin
from django.urls import path
from blog_app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('add_blog/', views.add_blog, name = 'add_blog'),
    path('about_blog/', views.about_blog, name = 'about_blog'),
    path('<int:id>/', views.update_blog,name = 'update_blog' ),
    path('delete/<int:id>/', views.delete_blog,name = 'delete_blog' ),
]
    