from django.contrib import admin
from .models import Books

# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher_name', 'created_at', 'updated_at')
