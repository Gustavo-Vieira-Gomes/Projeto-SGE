from django.urls import path
from categories.views import CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView, CategoryCreateListAPIView, CategoryRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('categories/list/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('api/v1/categories/', CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy-api-view')
]