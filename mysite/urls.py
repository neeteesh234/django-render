"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the current directory, or adjust as needed

urlpatterns = [
    path("admin/", admin.site.urls),  
    # Include URLs from the 'myapp' application
    path("myapp/", include("myapp.urls")),  # Adjust 'myapp' to your actual app name
    path(" ", views.index, name="index"),  # Add a URL pattern for the home view
    path("home/", views.home, name="home"),  # Add a URL pattern for the home view.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files in development
