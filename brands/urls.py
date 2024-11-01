from django.urls import path
from brands.views import BrandListView, BrandCreateView, BrandDetailView, BrandUpdateView, BrandDeleteView, BrandCreateListAPIView, BrandRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brand_list'),
    path('brands/create/', BrandCreateView.as_view(), name='brands_create'),
    path('brands/<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),

    path('api/v1/brands/', BrandCreateListAPIView.as_view(), name='brand-create-list-api-view'),
    path('api/v1/brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-retrieve-update-destroy-api-view')
]