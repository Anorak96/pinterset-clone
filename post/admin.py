from django.contrib import admin
from .models import Pin, Tag

@admin.register(Pin)
class PinAdmin(admin.ModelAdmin):
    list_display = ('pk', 'profile', 'pin','created', 'description')
    list_filter = ('created', 'profile',)
    fieldsets = (
        (None, {'fields': ('profile', 'pin', 'description', 'tag')}),
    )
    readonly_fields = ('created',)
    list_per_page = 20

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    # list_filter = ('created', 'profile',)
    fieldsets = (
        (None, {'fields': ('tag',)}),
    )
    list_per_page = 20