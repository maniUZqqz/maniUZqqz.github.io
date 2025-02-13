from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us_page'),
    path('about/', views.about, name='about'),
    path('create-profile/', views.CreateProfileView.as_view(), name='create_profile_page'),
]
