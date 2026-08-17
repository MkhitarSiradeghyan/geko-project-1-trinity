from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import FaqEntry


@admin.register(FaqEntry)
class FaqEntryAdmin(ModelAdmin):
    list_display = (
        "question",
        "is_active",
        "ordering",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "question",
        "answer",
    )