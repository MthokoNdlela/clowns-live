from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	url(r'^login/$', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"), 

    path('', views.troupe, name="home"),
    path('clowns/', views.clowns, name="clowns"),
    path('clients/<str:pk_test>/', views.clients, name="clients"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]