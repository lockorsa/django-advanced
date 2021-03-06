from django.urls import path

from server.apps.index import views as index

app_name = 'index'

urlpatterns = [
    path('', index.index, name='index'),
    path('contacts/', index.contact, name='contacts'),
]
