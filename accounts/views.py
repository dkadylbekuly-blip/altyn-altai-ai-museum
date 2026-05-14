from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _

from pages.models import RecognitionHistory


def login_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:cabinet")

    form = AuthenticationForm(request, data=request.POST or None)
    next_url = request.GET.get("next") or request.POST.get("next")

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if next_url:
                return redirect(next_url)

            return redirect("accounts:cabinet")

    return render(request, "accounts/login.html", {
        "form": form,
        "next": next_url,
        "page_title": _("Login"),
    })


def register_view(request):
    if request.user.is_authenticated:
        return redirect("accounts:cabinet")

    form = UserCreationForm(request.POST or None)
    next_url = request.GET.get("next") or request.POST.get("next")

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)

            if next_url:
                return redirect(next_url)

            return redirect("accounts:cabinet")

    return render(request, "accounts/register.html", {
        "form": form,
        "next": next_url,
        "page_title": _("Register"),
    })


@login_required
def cabinet_view(request):
    recognitions = (
        RecognitionHistory.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )

    return render(request, "accounts/cabinet.html", {
        "recognitions": recognitions,
        "page_title": _("Cabinet"),
    })


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("pages:home")

    return redirect("accounts:cabinet")