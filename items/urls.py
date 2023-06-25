from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('handheld/', views.handheld, name='handheld'),
    path('console/', views.console, name='console'),
    path('accessory/', views.accessory, name='accessory'),
    path('games/', views.games, name='games'),
    path('sell-to-us/', views.sell_to_us, name='sell-to-us'),
    path('sale/', views.sale, name='sale'),
    path('<item_id>', views.item_detail, name='item_details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
