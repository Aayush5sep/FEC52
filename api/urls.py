from django.urls import path
from api import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('books/',views.BooksAPI),
    path('clothes/',views.ClothesAPI),
    path('miscellaneous/',views.MiscAPI),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
