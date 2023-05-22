from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("create/", views.CreateView, name="create"),
    path("edit/<int:id_blog>", views.EditView, name="update"),
    path("delete/<int:id_blog>", views.DeleteData, name="delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
