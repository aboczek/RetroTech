from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-success/<order_number>', views.checkout_success, name='checkout_success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
