from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('view_courses/', views.view_courses, name="view_courses"),
    path('create_courses/', views.create_courses, name="create_courses"),
    path('delete_course/<int:item_id>/', views.delete_course, name="delete_course"),
    path('edit_course/<int:item_id>/', views.edit_course, name="edit_course"),
    

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    




