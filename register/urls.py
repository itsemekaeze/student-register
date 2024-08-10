from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('add-student', views.addPage, name='add-student'),
    path('delete-student/<int:id>/', views.deletePage, name='delete-student'),
    path('view-student/<int:id>/', views.viewPage, name='view-student'),
]