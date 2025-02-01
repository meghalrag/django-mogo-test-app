from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

def user_form_view(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            User(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                age=form.cleaned_data["age"]
            ).save()
            return redirect("user_list")
    else:
        form = UserForm()

    return render(request, "user_form.html", {"form": form})

def user_list_view(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})
