from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq, name='faq'),
    path('track-your-order/', views.track_your_order, name='tracking'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
