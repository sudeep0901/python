from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='blogs'),
    path('<int:blog_id>/', views.detail, name='blogdetail')

]

