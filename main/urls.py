from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main_page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pet/', views.about_my_pet, name='about_my_pet'),
    path('system_time/', views.system_time, name='system_time'),
    path('', include('main_page.urls')),
    path('', include('hashtags.urls')),
    path('', include('basket.urls')),
    path('', include('cbv.urls')),
    path('', include('parcing_books.urls')),
    path('', include("users.urls")),





]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
            document_root=settings.STATIC_ROOT)