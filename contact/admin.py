from django.contrib import admin
from .models import NewsletterSubscriber, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('name', 'email', 'subject')


admin.site.register(NewsletterSubscriber)
admin.site.register(Contact, ContactAdmin)