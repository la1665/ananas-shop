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
    #TODO
    # Comment:
    #TODO
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)