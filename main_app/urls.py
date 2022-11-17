from django.urls import path
# the . represents the current working directory
# we want to import the views since they are the functions that will bring our
# templates to the screen for our viewers
from . import views

urlpatterns = [
  # swag related routes
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('swag/', views.swag_index, name='index'),
  path('swag/<int:swag_id>/', views.swag_detail, name='detail'),
  path('swag/create/', views.SwagCreate.as_view(), name='swag_create'),
  path('swag/<int:pk>/update/', views.SwagUpdate.as_view(), name='swag_update'),
  path('swag/<int:pk>/delete/', views.SwagDelete.as_view(), name='swag_delete'),
  path('swag/<int:swag_id>/add_cleaning', views.add_cleaning, name='add_cleaning'),
  # set related routes
  path('sets/', views.SetList.as_view(), name='sets_index'),
  path('sets/<int:pk>/', views.SetDetail.as_view(), name='sets_detail'),
  path('sets/create/', views.SetCreate.as_view(), name='sets_create'),
  path('sets/<int:pk>/update/', views.SetUpdate.as_view(), name='sets_update'),
  path('sets/<int:pk>/delete/', views.SetDelete.as_view(), name='sets_delete'),
]