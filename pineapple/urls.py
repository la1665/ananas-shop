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
    path("comment-create/", views.views_comments.comment_create_view, name="comment-create"),
    path("seller-comment-list/<str:certificate_code>/", views.views_comments.seller_comment_list_view , name="seller-comment-list"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)