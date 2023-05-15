from django.urls import path
from users import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('loginpage/',views.loginpage),
    path('login/',views.loginuser),
    path('newaccnt/',views.signupuser),
    path('orgnaccnt/',views.signuporgn),
    path('newaccntpage/',views.signuppage),
    path('orgnpage/',views.orgnsignuppage),
    path('logout/',views.logoutuser),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
