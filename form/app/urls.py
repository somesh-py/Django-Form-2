from django.urls import path
from . import views

urlpatterns = [
    path('',views.showdata),
    path('add/',views.add),
    path('delete/<int:id>/',views.delete),
]
