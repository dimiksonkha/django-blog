from django.urls import path
from backend import views

#TEMPLATE TAGGING
app_name = 'backend'
urlpatterns = [
    path('posts/', views.posts, name='posts'),

]
