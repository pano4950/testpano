from django.contrib import admin

# Register your models here.
from .models import Session
@admin.register(Session)

class SessionAdmin (admin.ModelAdmin):
    list_display =('name', 'created_at')
    search_fields =('name',)
    ordering =('created_at',)