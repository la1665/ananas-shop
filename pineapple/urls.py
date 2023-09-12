from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    # Subscription:
    #TODO
    # Seller:
    #TODO
    # Pineapple:
    #TODO
    # Order:
    path("order-list/", views.views_orders.order_list_view, name="order-list"),
    path("order-detail/<int:pk>/", views.views_orders.order_detail_view, name="order-detail"),
    path("order-create/", views.views_orders.order_create_view, name="order-create"),
    path("order-update/<int:pk>/", views.views_orders.order_update_view, name="order-update"),
    # Comment:
    #TODO
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)