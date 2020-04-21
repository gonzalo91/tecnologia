from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="admin.index"),    

    path('products', views.IndexView.as_view(), name='product_index'),    
    path('product/edit/<int:pk>/', views.edit, name='product_edit'),

    path('newproduct/', views.productview, name='new_product'),
    path('delete/<int:pk>/', views.delete, name='product_delete'),
]