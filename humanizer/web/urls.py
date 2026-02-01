from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ai-detector/", views.ai_detector, name="ai_detector"),
    path("humanizer/", views.humanizer, name="humanizer"),
    path("grammar-checker/", views.grammar_checker, name="grammar_checker"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
