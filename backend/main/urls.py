from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product_catalog/', views.ProductsView.as_view(), name='product'),
    path('faq/', views.faq, name='faq'),
    path('order/', views.order, name='order'),
    path('reg/', views.add, name='add'),

]

