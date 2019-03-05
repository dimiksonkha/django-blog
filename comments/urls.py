from django.urls import path
from comments import views

#TEMPLATE TAGGING
app_name = 'comments'

urlpatterns = [
    path('submit_comment', views.submit_comment, name='submit_comment'),
    path('submit_reply', views.submit_reply, name='submit_reply'),

]
