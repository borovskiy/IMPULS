from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from .views import LoginView, Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logut/', LogoutView.as_view(), name='logout'),
]