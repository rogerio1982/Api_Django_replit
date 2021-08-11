

#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # add this

router.register(r'project', views.TodoView, 'project')
router.register(r'marvel', views.TodoView2, 'marvel')
router.register(r'ioga', views.TodoView3, 'ioga')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

