from django.urls import path
from reports import views

urlpatterns = [
    path('', views.index),
    path('companys/', views.CompanysListView.as_view())
]
