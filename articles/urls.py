from django.urls import path
from articles import views


app_name = 'articles'
urlpatterns = [
    path('', views.articles_list, name="list"),
    path('new/', views.articles_new, name='new'),
    path('<str:slug>/', views.articles_detail, name="detail"),
    path('<str:slug>/edit/', views.articles_update, name="update"),
    path('<str:slug>/delete/', views.articles_delete, name="delete"),
]