
from django.contrib import admin
from .models import ExcelFile

class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'uploaded_at')  # Display these fields in the admin list view
    ordering = ('-uploaded_at',)  # Order by upload date

admin.site.register(ExcelFile, ExcelFileAdmin)
