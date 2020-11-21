from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name="home"),
    path('test1/', views.test1, name="test1"),
    path('test2/', views.test2, name="test2"),
    path('register/', views.register, name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="home"), name="logout"),
]
