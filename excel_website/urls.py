from django.contrib import admin
from django.urls import path
from data_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_file, name='upload_file'),
    path('data/', views.view_data, name='view_data'),
]
