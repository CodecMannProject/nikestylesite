"""kukurudzo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from main import views
from main.views import SearchResultsView
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from main import views as user_views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path("search", SearchResultsView.as_view(), name='search_results'),
    path("users/search", SearchResultsView.as_view(), name='search_users'),
    path("users/pavlusha/search", SearchResultsView.as_view(), name='search_pavlusha'),
    path('users/pavlusha/', views.pavlusha, name='pavlusha'),
    path('users/yava/', views.yava, name='yava'),
    path('users/yava/popup.html', views.popup),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('events/', views.events, name='events'),
    path('projects/', views.projects, name='projects'),
    path('free-robux/', views.freerobux, name='robux'),
    path('files/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
]

handler404 = "main.views.error404"
handler500 = "main.views.error500"
handler403 = "main.views.error403"
handler400 = "main.views.error400"
