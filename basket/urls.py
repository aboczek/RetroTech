from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('basket/', views.view_basket, name='view_basket'),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('update/<item_id>/', views.update_basket, name='update_basket'),
    path('remove/<item_id>/', views.remove_from_basket,
         name='remove_from_basket'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
