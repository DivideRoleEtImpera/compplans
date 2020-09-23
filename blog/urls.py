from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.post_list, name='post_list'),
    path('plans/', views.plan_list, name='plan_list'),
    path('plans/plan/<str:id>/', views.plan, name='plan'),
    path('plans/new/', views.plan_new, name='plan_new'),
    path('plans/<int:id>/edit/', views.plan_edit, name='plan_edit')

 
]