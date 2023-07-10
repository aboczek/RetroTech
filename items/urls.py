from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('all/', views.all_items, name='all_items'),
    path('games/', views.games, name='games'),
    path('sell-to-us/', views.sell_to_us, name='sell_to_us'),
    path('sale/', views.sale, name='sale'),
    path('<int:item_id>', views.item_detail, name='item_details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
