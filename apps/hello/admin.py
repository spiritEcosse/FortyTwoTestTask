from django.contrib import admin
from apps.hello.models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', )

admin.site.register(Contacts, ContactsAdmin)