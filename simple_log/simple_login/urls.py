from django.contrib import admin
from django.urls import path, re_path, include
from apps.users import views as views
from django.conf.urls import url, include
from django.urls import reverse_lazy
from django.contrib.auth.views import  logout_then_login, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    # url('user/', include('users.urls', namespace = 'usuario')),
    # Sección para usuarios
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('accounts/login/', views.login),
    path('logout', views.logout),
    path('admin/', admin.site.urls),
    path('reset/password_reset',  PasswordResetView.as_view(), 
        {'template_name':'password_reset_form.html',
        'email_template_name': 'password_reset_email.html'}, 
        name='password_reset'), 
    path('password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'password_reset_done.html'}, 
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    path('reset/done', PasswordResetCompleteView.as_view(), {'redirect_to_login': 'users/login.html'},
        name='password_reset_complete'),
]
