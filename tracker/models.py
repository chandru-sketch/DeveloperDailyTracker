from django.db import models
from django.contrib.auth.models import User


class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    day = models.PositiveIntegerField()

    date = models.DateField(auto_now_add=True)

    english_words = models.BooleanField(default=False)
    english_speaking = models.BooleanField(default=False)
    reading = models.BooleanField(default=False)

    interview = models.BooleanField(default=False)

    python_topic = models.BooleanField(default=False)
    coding_problem = models.BooleanField(default=False)
    mini_program = models.BooleanField(default=False)

    html_css_js = models.BooleanField(default=False)
    ui_component = models.BooleanField(default=False)

    sql_django = models.BooleanField(default=False)

    project = models.BooleanField(default=False)

    github = models.BooleanField(default=False)

    typing = models.BooleanField(default=False)

    notes = models.BooleanField(default=False)

    revision = models.BooleanField(default=False)

    sleep = models.BooleanField(default=False)

    achievement = models.TextField(blank=True)

    challenges = models.TextField(blank=True)

    tomorrow_focus = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Day {self.day}"
    
class Goal(models.Model):

    PRIORITY = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY,
        default="Medium"
    )

    due_date = models.DateField()

    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.contrib.auth.models import User

class UserSettings(models.Model):

    THEME_CHOICES = [
        ("light", "Light"),
        ("dark", "Dark"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="settings"
    )

    theme = models.CharField(
        max_length=10,
        choices=THEME_CHOICES,
        default="light"
    )

    daily_reminder = models.BooleanField(default=True)

    weekly_report = models.BooleanField(default=True)

    email_notifications = models.BooleanField(default=True)

    profile_public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Settings"