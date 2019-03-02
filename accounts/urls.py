from django.urls import path
from accounts import views

#TEMPLATE TAGGING
app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('sign-up/', views.registration, name='sign-up'),
]
