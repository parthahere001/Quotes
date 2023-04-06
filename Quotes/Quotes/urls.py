from django.contrib import admin
from django.urls import path, include
from mainapp import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('wel/', views.backendfunction, basename='backend')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('dar/', views.backendfunction, name='some'),
    path('dar/<int:pk>', views.backendfunction, name = 'some2'),
]
