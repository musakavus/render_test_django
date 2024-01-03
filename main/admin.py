from django.contrib import admin

from main.models import ContactMessageModel


# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'subject', 'message', 'formatted_send_at')
    search_fields = ('full_name', 'email', 'subject')


admin.site.register(ContactMessageModel, ContactMessageAdmin)
