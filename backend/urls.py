from django.urls import path
from backend import views

#TEMPLATE TAGGING
app_name = 'backend'
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('users/', views.users, name='users'),
    path('comments/', views.comments, name='comments'),
    path('tags/', views.tags, name='tags'),
    path('categories/', views.categories, name='categories'),
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),

]
