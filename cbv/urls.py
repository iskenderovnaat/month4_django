from django.urls import path
from . import views

urlpatterns = [
    path('order_list_class/', views.OrderListView.as_view(), name='order_list_class'),
    path('basket_class/<int:id>/update/', views.UpdateOrderView.as_view(), name='update'),
    path('basket_class/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete'),
    path('/create_class/', views.CreateOrderView.as_view(), name='create_class'),

]