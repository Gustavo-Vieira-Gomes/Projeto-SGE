from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from products.models import Product
from django.urls import reverse_lazy
from products.forms import ProductForm
from categories.models import Category
from brands.models import Brand
from app.metrics import get_product_metrics
from rest_framework import generics
from .serializers import ProductSerializer

# Create your views here.


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        serie_number = self.request.GET.get('serie_number')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if category:
            queryset = queryset.filter(category__id=category)

        if brand:
            queryset = queryset.filter(brand__id=brand)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = get_product_metrics()
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.create_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    form_class = ProductForm
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'


class ProductCreateListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all
    serializer_class = ProductSerializer
