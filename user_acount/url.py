from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.handle_login, name="handle_login"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




