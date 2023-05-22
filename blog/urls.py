from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView, name="index"),
    path("create/", views.CreateView, name="create"),
    path("edit/<int:id_blog>", views.EditView, name="update"),
    path("delete/<int:id_blog>", views.DeleteData, name="delete"),
]
