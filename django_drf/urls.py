from . import signals
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .services import admin_replenish_stock
from .views import ProductViewSet, ReviewViewSet, CategoryViewSet, OrderViewSet
from .services.flash_sale import check_flash_sale,FlashListCreateView
from .services.product_view_history import ProductViewHistoryCreate

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'orders',OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('sale/',FlashListCreateView.as_view(),name='sale'),
    path('check-sale/<int:product_id>/', check_flash_sale, name='product-view-history-create'),
    path('product_view/',ProductViewHistoryCreate.as_view(),name='product-view-history-create'),
    path('admin/replenish_stock/<int:product_id>/<int:amount>',admin_replenish_stock,name='admin_replenish_stock'),

]