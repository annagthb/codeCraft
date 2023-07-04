from django.contrib import admin
from django.urls import path, include
from webDjangoProject.views import helloWorld
from . import views

urlpatterns = [
    path('',views.create_root_view),#root URL which calls templates/create_root_view.html
    #path('',views.index)#root URL simple index HttpResponse
    path('list/',views.list_view),
    path('<int:id>/', views.detail_view ),
    path('<int:id>/delete', views.delete_view ),
   ]