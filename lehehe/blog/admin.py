from django.contrib import admin

# Register your models here.
from .models import Algorithm
@admin.register(Algorithm)
class AlgorithmAdmin(admin.ModelAdmin):
    list_display = ("algo_name", "algo_author", "update_time")
    list_filter = ("update_time", "algo_author")
    search_fields = ("algo_name", "algo_content")
    raw_id_fields = ("algo_author",)
    date_hierarchy = "update_time"
    ordering = ["update_time", "algo_author"]

