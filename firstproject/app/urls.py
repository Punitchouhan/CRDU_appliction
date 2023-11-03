from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("ragistration/",views.ragistration),
    path("table/",views.table),
    path("delete/<int:pk>/",views.userdelete,name='delete'),
    path("sing_up/",views.sing_up),
]