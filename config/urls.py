from django.contrib import admin
from django.urls import path

from apiv1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', views.BookCreateAPIView.as_view()),
    path('api/v1/books/<pk>/', views.BookUpdateAPIView.as_view()),
]
