from django.urls import path
from blog import views

#TEMPLATE TAGGING
app_name = 'blog'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('sign-up/', views.registration, name='sign-up'),
    path('<int:year>/', views.archeive_posts, name='archeive_post'),
    path('<int:year>/<int:month>/<int:day>/', views.archeive_posts_by_date, name='archeive_date'),
    path('tag/<str:tag>/', views.archeive_posts_by_tag, name='archeive_tag'),
    path('category/<str:category>/', views.archeive_posts_by_category, name='archeive_category'),
    path('author/<str:username>/', views.archeive_posts_by_author, name='archeive_author'),
    path('posts/<int:pk>/', views.post_details, name='post_details'),
    path('posts/search_result', views.search_view, name='search_view'),
    path('submit_comment', views.submit_comment, name='submit_comment'),
    path('submit_reply', views.submit_reply, name='submit_reply'),

]
