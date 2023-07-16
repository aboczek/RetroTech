from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('faq/', views.faq, name='faq'),
     path('track-your-order/', views.track_your_order, name='tracking'),
     path('user-account/', views.profile, name='profile'),
     path('front/', views.front_end_panel, name='front'),
     path('order-history/<order_number>',
          views.order_history,
          name='order-history'),
     path('edit-item/<item_id>', views.edit_item, name='edit-item'),
     path('delete-item/<item_id>', views.delete_item, name='delete-item'),
     path('newsletter-emails/',
          views.newsletter_email, name='newsletter-emails'),
     path('delete-email/<email_id>',
          views.delete_newsletter_email, name='delete-email'),
     path('sell-to-me/', views.sell_to_me, name='sell-to-me'),
     path('sell-details/<sell_id>',
          views.sell_to_me_details, name='sell-to-me-details'),
     path('terms-and-conditions/',
          views.terms_conditions, name='terms-conditions'),
     path('admin-orders/', views.admin_orders, name='admin-orders'),
     path('admin-orders-preview/<order_id>', views.admin_orders_preview, name='admin-orders-preview'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
