from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DailyTask

class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

        widgets = {

            "username": forms.TextInput(
                attrs={
                    "placeholder":"Username"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder":"Email Address"
                }
            )

        }

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

        self.fields["password1"].widget.attrs.update({
            "placeholder":"Password"
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder":"Confirm Password"
        })    
class DailyTaskForm(forms.ModelForm):

    class Meta:
        model = DailyTask

        fields = [
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
            "achievement",
            "challenges",
            "tomorrow_focus",
        ]

        widgets = {
            "achievement": forms.Textarea(attrs={
                "rows":3,
                "placeholder":"Today's Achievement"
            }),

            "challenges": forms.Textarea(attrs={
                "rows":3,
                "placeholder":"Challenges Faced"
            }),

            "tomorrow_focus": forms.Textarea(attrs={
                "rows":3,
                "placeholder":"Tomorrow's Focus"
            }),
        }

from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal

        fields = [
            "title",
            "description",
            "priority",
            "due_date",
        ]

        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

from .models import UserSettings

class UserSettingsForm(forms.ModelForm):

    class Meta:
        model = UserSettings
        fields = [
            "theme",
            "daily_reminder",
            "weekly_report",
            "email_notifications",
            "profile_public",
        ]

        widgets = {
            "theme": forms.Select(attrs={"class": "form-select"}),

            "daily_reminder": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

            "weekly_report": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

            "email_notifications": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),

            "profile_public": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }