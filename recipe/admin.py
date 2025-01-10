from django.contrib import admin

from .models import ContactModel, AboutModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject','created_at')
    search_fields = ('name','email','subject')

@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone','message','created_at')
    search_fields = ('name','email','phone')
    list_filter = ('phone',)