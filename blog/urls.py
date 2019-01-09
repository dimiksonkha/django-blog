from django.urls import path
from blog import views

#TEMPLATE TAGGING
app_name = 'blog'

urlpatterns = [
    path('sh/', views.index, name='index'),
    path('new_post/', views.post_form_view, name='new__post_form'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('sign-up/', views.registration, name='sign-up'),

]
