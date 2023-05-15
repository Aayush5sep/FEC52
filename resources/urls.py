from django.urls import path
from resources import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('bookdonate/',views.DonateBook),
    path('clothesdonate/',views.DonateClothes),
    path('miscdonate/',views.DonateMisc),
    path('bookreq/',views.RequestBook),
    path('clothesreq/',views.RequestClothes),
    path('miscreq/',views.RequestMisc),
    path('allresources/',views.AllResources),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
