from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('student/', views.getStudents),
    path('student/<int:id>/', views.getStudent),
]