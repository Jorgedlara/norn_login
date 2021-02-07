from django.contrib import admin
from django.urls import path
from apps.users import views as views

from django.conf.urls import url, include


urlpatterns = [
    # url(r'^user/', include('users.urls', namespace = 'usuario')),
    # Sección para usuarios
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('admin/', admin.site.urls),
]
