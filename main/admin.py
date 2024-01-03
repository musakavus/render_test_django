from django.contrib import admin

from main.models import ContactMessageModel


# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ContactMessageModel, ContactMessageAdmin)
