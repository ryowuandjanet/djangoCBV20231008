from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # (R) Read
    path("", views.Read.as_view(), name="read"),
    # (C) Create
    path("create/", views.Create.as_view(), name="create"),
    # (U) Update
    path("update/<int:pk>/", views.Update.as_view(), name="update"),
    # (D) Delete
    path("delete/<int:pk>/", views.Delete.as_view(), name="delete"),
]
