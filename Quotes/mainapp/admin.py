from django.contrib import admin
from .models import QuoteModel

@admin.register(QuoteModel)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id','name','details']