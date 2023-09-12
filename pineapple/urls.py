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
    path("pineapple-list/", views.views_pineapple.pineapple_list_view, name="pineapple-list"),
    path("pineapple-detail/<int:pk>/", views.views_pineapple.pineapple_detail_view, name="pineapple-detail"),
    path("pineapple-create/", views.views_pineapple.pineapple_create_view, name="pineapple-create"),
    path("pineapple-update/<int:pk>/", views.views_pineapple.pineapple_update_view, name="pineapple-update"),
    path("seller-pineapple-list/<int:seller_id>/", views.views_pineapple.seller_pineapple_list_view, name="seller-pineapple-list"),
    # Order:
    #TODO
    # Comment:
    #TODO
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)