from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_index, name='article_index'),
    path('article/<int:article_id>/', views.article_show, name='article_show'),
    path('article/<int:article_id>/delete/', views.article_delete, name='article_delete'),
    path('article/create/', views.article_create, name='article_create'),
    path('article/edit/<int:article_id>/', views.article_edit, name='article_edit'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]

