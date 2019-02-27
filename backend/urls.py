from django.urls import path
from backend import views

#TEMPLATE TAGGING
app_name = 'backend'
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts_by_author/', views.posts_by_author, name='posts_by_author'),
    path('new_post/', views.new_post, name='new_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/', views.update_post, name='update_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('users/', views.users, name='users'),
    path('comments/', views.comments, name='comments'),
    path('moderate_comment/', views.moderate_comment, name='moderate_comment'),
    path('moderate_user/', views.moderate_user, name='moderate_user'),
    path('update/', views.update_profile, name='update_profile'),
    path('tags/', views.tags, name='tags'),
    path('add_new_tag/', views.add_new_tag, name='add_new_tag'),
    path('categories/', views.categories, name='categories'),
    path('add_new_category', views.add_new_category, name="add_new_category"),
    path('settings/', views.settings, name='settings'),
    path('update_settings/', views.update_settings, name='update_settings'),
    path('profile/', views.profile, name='profile'),

]
