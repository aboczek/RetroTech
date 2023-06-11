from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('handheld/', views.handheld, name='handheld'),
    path('console/', views.console, name='console'),
    path('accessory/', views.accessory, name='accessory'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
