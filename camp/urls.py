from django.urls import path
from camp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.test),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
