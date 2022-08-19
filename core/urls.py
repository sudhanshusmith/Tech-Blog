from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_signup/', views.user_signup, name='user_signup'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('newpost/', views.newpost, name='newpost'),
    path('editpost/<int:id>/', views.editpost, name='editpost'),
    path('updatepost/<int:id>/', views.updatepost, name='updatepost'),
    path('confirm_del/<int:id>/', views.confirm_del, name='confirm_del'),
    path('deletepost/<int:id>/', views.deletepost, name='deletepost'),
    path('user_changepass/', views.user_changepass, name='user_changepass'),

    
]