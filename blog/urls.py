from django.urls import path
from blog import views

urlpatterns = [
    path('sh/', views.index, name='index'),

]
