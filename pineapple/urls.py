from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [
    # Subscription:
    path("subscription-create/", views.views_subscription.subscription_create_view, name="subscription-create"),
    path("subscription-list/", views.views_subscription.subscription_list_view, name="subscription-list"),
    # Seller:
    #TODO
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)