from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name="index"),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('change_passwrod/', views.change_passwrod, name='change_passwrod'),
    path('logout_user/', views.logout_user, name='logout_user'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




