from django.urls import path
from suppliers.views import SupplierListView, SupplierCreateView, SupplierDetailView, SupplierUpdateView, SupplierDeleteView, SupplierCreateListAPIView, SupplierRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('suppliers/list/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    path('api/v1/suppliers/', SupplierCreateListAPIView.as_view(), name='supplier-create-list-api-view'),
    path('api/v1/suppliers/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-retrieve-update-destroy-api-view')
]
