from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('', views.login, name='login'),
    # path('logout/', views.Logout, name='logout'),
    path('register/', views.RegisterView.as_view(), name='login'),
]