from django.contrib import admin
from .models import DailyTask


@admin.register(DailyTask)
class DailyTaskAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "day",
        "date",
    )

    search_fields = (
        "user__username",
    )

    list_filter = (
        "day",
    )

from .models import Goal

admin.site.register(Goal)