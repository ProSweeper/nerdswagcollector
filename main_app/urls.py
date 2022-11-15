from django.urls import path
# the . represents the current working directory
# we want to import the views since they are the functions that will bring our
# templates to the screen for our viewers
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('swag/', views.swag_index, name='index'),
    path('swag/<int:swag_id>/', views.swag_detail, name='detail')
]