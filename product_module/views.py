from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, View
from .models import Product






class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product



def cart(request):
    return render(request, 'product_module/cart.html', {})



def checkout(request):
    return render(request, 'product_module/checkout.html', {})


def profile(request):
    return render(request, 'login/profile.html', {})


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     load_product = self.object_list
    #     request = self.request
    #     favorite_product_id = request.session['favorite-list']
    #     context['is_favorite'] = favorite_product_id == str(load_product.id)
    #     return context


class FavoriteListView(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['favorite-list'] = product_id
        return redirect("home_page")









