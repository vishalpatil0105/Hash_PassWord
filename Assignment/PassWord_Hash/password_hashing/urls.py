
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home_page, name='home'),
   path('adduser/', views.add_new_user, name='add-new-user'),
   path('add_new_user/', views.add_user, name='add-user'),
]