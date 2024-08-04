from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('پرداخت/', views.checkout, name='checkout'),
    path("سبد-خرید/", views.cart, name="cart"),
    path("profile/", views.profile, name='profile'),
    path("/مورد-علاقه", views.FavoriteListView.as_view(), name='favorite-list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)