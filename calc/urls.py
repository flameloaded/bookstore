from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('calc', views.calc_page, name='calc'),
    path(r'([^/])', views.calc_pages, name='calc page' )
]
