
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import *


urlpatterns = [

    path("admin/", admin.site.urls),
    path("", home_route, name="home_route"),
    path("live_chat", faq_route, name="faq_route"),
    path("login", login_route, name="login_route"),
    path("contact", contact_route, name="contact_route"),
    path("join", join_route, name="join_route"),
    path("logout", logout_route, name="logout_route"),
    path("create_ticket", create_ticket, name="create_ticket"),
    path("open_tickets", open_tickets, name="open_tickets"),
    path("all_tickets", all_tickets, name="all_tickets"),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)