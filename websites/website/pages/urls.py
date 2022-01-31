from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home,name="Home"),
    path('contact', views.contact,name="Contact"),
    path('portfolio', views.portfolio,name="Portfolio"),
    path('about', views.about,name="About"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
