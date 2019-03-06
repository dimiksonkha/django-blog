"""
    blog_engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from backend import views
from accounts import views



# from django.conf.urls import (
#     handler500,
#     handler400,
#     handler403
# )



urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', include('blog.urls')),
    path('backend/', include('backend.urls')),
    path('accounts/', include('accounts.urls')),
    path('comments/', include('comments.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler500 = 'blog.views.custom_500'
# handler400 = 'blog.views.custom_400'
# handler403 = 'blog.views.custom_403'
