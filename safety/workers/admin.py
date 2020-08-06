from django.contrib import admin
from .models import Worker

# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'first_neme',
        'last_name',
        'is_available',
        'primary_phone',
        'secondary_phone',
    )