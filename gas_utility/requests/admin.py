from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'status', 'created_at', 'resolved_at')
    list_filter = ('service_type', 'status')
    search_fields = ('user__username', 'description')