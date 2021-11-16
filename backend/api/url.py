from django.urls import path
from . import views
app_name = 'backend'
urlpatterns = [ 
    path('Certificate/', views.CertificateListView.as_view(), name='Certificate_list'), 
    path('Certificate/<pk>/', views.CertificateDetailView.as_view(), name='Certificate_detail'),
    path('Service/', views.ServiceListView.as_view(), name='Service_list'), 
    path('Service/<pk>/', views.ServiceDetailView.as_view(), name='Service_detail'),
    path('Product/', views.ProductListView.as_view(), name='Product_list'), 
    path('Product/<pk>/', views.ProductDetailView.as_view(), name='Product_detail'),
]