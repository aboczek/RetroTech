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
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
