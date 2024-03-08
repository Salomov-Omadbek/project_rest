from django.contrib import admin
from .models import Book,Rating

admin.site.register(Book)
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating']
    list_filter = ['user', 'book', 'rating']
# views.py (continued)

