from django.urls import path

from server.apps.authapp import views as auth

app_name = 'authapp'

urlpatterns = [
    path('register/', auth.register, name='register'),
    path('login/', auth.login, name='login'),
    path('logout/', auth.logout, name='logout'),
    path('edit/', auth.edit, name='edit'),
    path('verify/<email>/<key>/', auth.verify, name='verify'),
]
