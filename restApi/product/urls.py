from django.urls import path, include
from . import views

urlpatterns = [
    path('category/', include([
        path('', views.CategoryMixinsView.as_view(), name='category-list'),
        path('<int:pk>/', views.CategoryMixinsView.as_view(), name='category-detail'),
        path('create/', views.CategoryMixinsView.as_view(), name='category-create'),
        path('update/<int:pk>/', views.CategoryMixinsView.as_view(), name='category-update'),
        path('delete/<int:pk>/', views.CategoryMixinsView.as_view(), name='category-delete'),
    ])),

    path('product/<int:pk>/', views.DetailProductView.as_view(), name='product-detail'),
]
