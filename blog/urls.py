from django.urls import path
from blog import views

urlpatterns = [
    path('sh/', views.index, name='index'),
    path('new_post/', views.post_form_view, name='new__post_form'),

]
