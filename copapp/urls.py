from django.contrib import admin
from django.urls import path
from .views import index, contato, chaves

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('chaves', chaves, name='chaves')
]