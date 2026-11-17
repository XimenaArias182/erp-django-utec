# reportes/urls.py
from django.urls import path
from . import views

app_name = 'reportes'

urlpatterns = [
    path('', views.ReporteListView.as_view(), name='lista'),
    path('', views.ReporteListView.as_view(), name='inicio'),
]