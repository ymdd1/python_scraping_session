from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="scraping_index"),
    # スプレッドシートへの書き込み処理
    path("gs", views.gs, name="scraping_gs"),
]
