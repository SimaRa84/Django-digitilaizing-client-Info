from django.urls import path
from . import views
urlpatterns = [
     path('create/', views.create_bank_form, name='create'),
] 