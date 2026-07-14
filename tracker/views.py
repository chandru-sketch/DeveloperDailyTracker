from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .forms import RegisterForm, DailyTaskForm
from .models import DailyTask


def home(request):
    return render(request, "tracker/home.html")

def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(
        request,
        "tracker/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            return redirect("dashboard")

    else:

        form = AuthenticationForm()

    return render(
        request,
        "tracker/login.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    return redirect("home")

@login_required
def dashboard(request):

    current_day = int(request.GET.get("day", 1))

    task, created = DailyTask.objects.get_or_create(
        user=request.user,
        day=current_day
    )

    if request.method == "POST":

        form = DailyTaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect(f"/dashboard/?day={current_day}")

    else:

        form = DailyTaskForm(instance=task)

    checkbox_fields = [
        "english_words",
        "english_speaking",
        "reading",
        "interview",
        "python_topic",
        "coding_problem",
        "mini_program",
        "html_css_js",
        "ui_component",
        "sql_django",
        "project",
        "github",
        "typing",
        "notes",
        "revision",
        "sleep",
    ]

    completed = sum(
        getattr(task, field)
        for field in checkbox_fields
    )

    progress = int((completed / len(checkbox_fields)) * 100)

    # Create 30-day calendar data
    days = []

    for i in range(1, 31):
        days.append({
            "number": i,
            "completed": i < current_day,
            "current": i == current_day,
        })

    context = {
        "form": form,
        "task": task,
        "progress": progress,
        "completed": completed,
        "total": len(checkbox_fields),
        "current_day": current_day,
        "days": days,
    }

    return render(request, "tracker/dashboard.html", context)
from django.contrib.auth.decorators import login_required

@login_required
def progress(request):
    return render(request, "tracker/progress.html")


from .models import Goal
from .forms import GoalForm

@login_required
def goals(request):

    goals = Goal.objects.filter(user=request.user)

    if request.method == "POST":

        form = GoalForm(request.POST)

        if form.is_valid():

            goal = form.save(commit=False)

            goal.user = request.user

            goal.save()

            return redirect("goals")

    else:

        form = GoalForm()

    return render(
        request,
        "tracker/goals.html",
        {
            "form": form,
            "goals": goals,
        },
    )

@login_required
def profile(request):
    return render(request, "tracker/profile.html")


from .models import UserSettings
from .forms import UserSettingsForm


@login_required
def settings_page(request):

    settings_obj, created = UserSettings.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = UserSettingsForm(
            request.POST,
            instance=settings_obj
        )

        if form.is_valid():

            form.save()

            return redirect("settings")

    else:

        form = UserSettingsForm(instance=settings_obj)

    return render(
        request,
        "tracker/settings.html",
        {
            "form": form,
        },
    )

@require_POST
@login_required
def save_theme(request):

    data = json.loads(request.body)

    theme = data.get("theme", "light")

    settings = request.user.settings

    settings.theme = theme

    settings.save()

    return JsonResponse({
        "success": True,
        "theme": theme,
    })