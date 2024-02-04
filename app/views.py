from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_now, logout as logout_now
from .models import *


def home_route(request):
    context = {}
    return render(request, "home_route.html", context)


def contact_route(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        email = request.POST.get("email")
        contact = Contact(fullname=name, mobile = mobile, address=address, email=email)
        contact.save()
    context = {}
    return render(request, "contact_route.html", context)


def faq_route(request):
    context = {}
    return render(request, "faq_route.html", context)
    

def login_route(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login_now(request, user)
            return redirect("home_route")
    context = {}
    return render(request, "login_route.html", context)


def join_route(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        account_number = request.POST.get("account_number")
        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        user = User.objects.create_user(username = username, first_name = full_name, last_name = account_number, email = email, password = password)
        user.save()
        return redirect("login_route")
    context = {}
    return render(request, "join_route.html", context)


def logout_route(request):
    logout_now(request)
    return redirect("login_route")


def create_ticket(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        issue = request.POST.get("issue")
        ticket = Ticket(user = request.user, subject = subject, issue=issue, status=False)
        ticket.save()
        return redirect("open_tickets")
    context = {}
    return render(request, "create_ticket.html", context)


def open_tickets(request):
    tickets = Ticket.objects.filter(user = request.user, status=False).all()
    context = {"tickets":tickets}
    return render(request, "manage_tickets.html", context)


def all_tickets(request):
    tickets = Ticket.objects.filter(user = request.user)
    context = {"tickets":tickets}
    return render(request, "all_tickets.html", context)