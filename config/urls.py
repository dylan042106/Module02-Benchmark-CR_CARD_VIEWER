from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.home_page_view),
    path("<card_name>/", views.singleCardPageView),
    path("admin/", admin.site.urls),
]
