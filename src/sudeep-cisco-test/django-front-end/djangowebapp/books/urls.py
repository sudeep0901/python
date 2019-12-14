from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /books/5/
    path('<int:isbn_id>/', views.detail, name='detail'),
    # ex: /books/5/results/
    # path('<int:isbn_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('createForm', views.create, name='create'),
    path('create', views.create, name='create'),
    path('^delete/<int:isbn_id>/', views.delete, name='delete'),

]


